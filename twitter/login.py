import sys
from httpx import Client
from .constants import GREEN, YELLOW, RED, BOLD, RESET
from .util import find_key, get_confirmation_code, get_inbox, init_session


def update_token(session: Client, key: str, url: str, **kwargs) -> Client:
    caller_name = sys._getframe(1).f_code.co_name
    try:
        headers = {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36',
            'x-guest-token': session.cookies.get('guest_token', ''),
            'x-csrf-token': session.cookies.get('ct0', ''),
            'x-twitter-auth-type': 'OAuth2Client' if session.cookies.get('auth_token') else '',
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en',
        }
        r = session.post(url, headers=headers, **kwargs)
        info = r.json()

        print(f'{info = }')

        for task in info.get('subtasks', []):
            if task.get('enter_text', {}).get('keyboard_type') == 'email':
                print(f"[{YELLOW}warning{RESET}] {' '.join(find_key(task, 'text'))}")
                session.cookies.set('confirm_email', 'true')  # signal that email challenge must be solved

            if task.get('subtask_id') == 'LoginAcid':
                if task['enter_text']['hint_text'].casefold() == 'confirmation code':
                    print(f"[{YELLOW}warning{RESET}] email confirmation code challenge.")
                    session.cookies.set('confirmation_code', 'true')

        session.cookies.set(key, info[key])

    except KeyError as e:
        session.cookies.set('flow_errors', 'true')  # signal that an error occurred somewhere in the flow
        print(f'[{RED}error{RESET}] failed to update token at {BOLD}{caller_name}{RESET}\n{e}')
    return session


def init_guest_token(session: Client) -> Client:
    return update_token(session, 'guest_token', 'https://api.twitter.com/1.1/guest/activate.json')


def flow_start(session: Client) -> Client:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json',
                        params={'flow_name': 'login'},
                        json={
                            "input_flow_data": {
                                "flow_context": {
                                    "debug_overrides": {},
                                    "start_location": {"location": "splash_screen"}
                                }
                            }, "subtask_versions": {}
                        })


def flow_instrumentation(session: Client) -> Client:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginJsInstrumentationSubtask",
            "js_instrumentation": {"response": "{}", "link": "next_link"}
        }],
    })


def flow_username(session: Client) -> Client:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginEnterUserIdentifierSSO",
            "settings_list": {
                "setting_responses": [{
                    "key": "user_identifier",
                    "response_data": {"text_data": {"result": session.cookies.get('username')}}
                }], "link": "next_link"}}],
    })


def flow_password(session: Client) -> Client:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginEnterPassword",
            "enter_password": {"password": session.cookies.get('password'), "link": "next_link"}}]
    })


def flow_duplication_check(session: Client) -> Client:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "AccountDuplicationCheck",
            "check_logged_in_account": {"link": "AccountDuplicationCheck_false"},
        }],
    })


def confirm_email(session: Client) -> Client:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [
            {
                "subtask_id": "LoginAcid",
                "enter_text": {
                    "text": session.cookies.get('email'),
                    "link": "next_link"
                }
            }]
    })


def solve_confirmation_challenge(session: Client, email: str, password: str) -> Client:
    proton_session = init_session(email, password)
    inbox = get_inbox(proton_session)
    confirmation_code = get_confirmation_code(inbox)
    print(f'{confirmation_code = }')
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": session.cookies.get('flow_token'),
        'subtask_inputs': [
            {
                'subtask_id': 'LoginAcid',
                'enter_text': {
                    'text': confirmation_code,
                    'link': 'next_link',
                },
            },
        ],
    })


def execute_login_flow(session: Client) -> Client | None:
    session = init_guest_token(session)
    for fn in [flow_start, flow_instrumentation, flow_username, flow_password, flow_duplication_check]:
        session = fn(session)

    # solve email challenge
    if session.cookies.get('confirm_email') == 'true':
        session = confirm_email(session)

    # solve confirmation challenge (Proton Mail only)
    if session.cookies.get('confirmation_code') == 'true':
        if not session.protonmail:
            print(f'[{RED}warning{RESET}] Please check your email for a confirmation code'
                  f' and log in again using the web app. If you wish to automatically solve'
                  f' email confirmation challenges, add a Proton Mail account in your account settings')
            return
        session = solve_confirmation_challenge(session, *session.protonmail.values())
    return session


def login(email: str, username: str, password: str, **kwargs) -> Client:
    session = Client()
    session.cookies.update({
        "email": email,
        "username": username,
        "password": password,
        "guest_token": None,
        "flow_token": None,
    })
    session.protonmail = kwargs.get('protonmail')
    session = execute_login_flow(session)
    if not session or session.cookies.get('flow_errors') == 'true':
        print(f'[{RED}error{RESET}] {BOLD}{username}{RESET} login failed')
    else:
        print(f'[{GREEN}success{RESET}] {BOLD}{username}{RESET} login success')
    return session
