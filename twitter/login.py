import sys

from httpx import Client

from .constants import GREEN, YELLOW, RED, BOLD, RESET
from .util import find_key  # ,get_confirmation_code, get_inbox, init_protonmail_session


def update_token(client: Client, key: str, url: str, **kwargs) -> Client:
    caller_name = sys._getframe(1).f_code.co_name
    try:
        headers = {
            'x-guest-token': client.cookies.get('guest_token', ''),
            'x-csrf-token': client.cookies.get('ct0', ''),
            'x-twitter-auth-type': 'OAuth2Client' if client.cookies.get('auth_token') else '',
        }
        client.headers.update(headers)
        r = client.post(url, **kwargs)
        info = r.json()

        for task in info.get('subtasks', []):
            if task.get('enter_text', {}).get('keyboard_type') == 'email':
                print(f"[{YELLOW}warning{RESET}] {' '.join(find_key(task, 'text'))}")
                client.cookies.set('confirm_email', 'true')  # signal that email challenge must be solved

            if task.get('subtask_id') == 'LoginAcid':
                if task['enter_text']['hint_text'].casefold() == 'confirmation code':
                    print(f"[{YELLOW}warning{RESET}] email confirmation code challenge.")
                    client.cookies.set('confirmation_code', 'true')

        client.cookies.set(key, info[key])

    except KeyError as e:
        client.cookies.set('flow_errors', 'true')  # signal that an error occurred somewhere in the flow
        print(f'[{RED}error{RESET}] failed to update token at {BOLD}{caller_name}{RESET}\n{e}')
    return client


def init_guest_token(client: Client) -> Client:
    return update_token(client, 'guest_token', 'https://api.twitter.com/1.1/guest/activate.json')


def flow_start(client: Client) -> Client:
    return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json',
                        params={'flow_name': 'login'},
                        json={
                            "input_flow_data": {
                                "flow_context": {
                                    "debug_overrides": {},
                                    "start_location": {"location": "splash_screen"}
                                }
                            }, "subtask_versions": {}
                        })


def flow_instrumentation(client: Client) -> Client:
    return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": client.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginJsInstrumentationSubtask",
            "js_instrumentation": {"response": "{}", "link": "next_link"}
        }],
    })


def flow_username(client: Client) -> Client:
    return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": client.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginEnterUserIdentifierSSO",
            "settings_list": {
                "setting_responses": [{
                    "key": "user_identifier",
                    "response_data": {"text_data": {"result": client.cookies.get('username')}}
                }], "link": "next_link"}}],
    })


def flow_password(client: Client) -> Client:
    return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": client.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginEnterPassword",
            "enter_password": {"password": client.cookies.get('password'), "link": "next_link"}}]
    })


def flow_duplication_check(client: Client) -> Client:
    return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": client.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "AccountDuplicationCheck",
            "check_logged_in_account": {"link": "AccountDuplicationCheck_false"},
        }],
    })


def confirm_email(client: Client) -> Client:
    return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
        "flow_token": client.cookies.get('flow_token'),
        "subtask_inputs": [
            {
                "subtask_id": "LoginAcid",
                "enter_text": {
                    "text": client.cookies.get('email'),
                    "link": "next_link"
                }
            }]
    })


# def solve_confirmation_challenge(client: Client, email: str, password: str) -> Client:
#     proton_session = init_protonmail_session(email, password)
#     inbox = get_inbox(proton_session)
#     confirmation_code = get_confirmation_code(inbox)
#     print(f'{confirmation_code = }')
#     return update_token(client, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', json={
#         "flow_token": client.cookies.get('flow_token'),
#         'subtask_inputs': [
#             {
#                 'subtask_id': 'LoginAcid',
#                 'enter_text': {
#                     'text': confirmation_code,
#                     'link': 'next_link',
#                 },
#             },
#         ],
#     })


def execute_login_flow(client: Client) -> Client | None:
    client = init_guest_token(client)
    for fn in [flow_start, flow_instrumentation, flow_username, flow_password, flow_duplication_check]:
        client = fn(client)

    # solve email challenge
    if client.cookies.get('confirm_email') == 'true':
        client = confirm_email(client)

    # # solve confirmation challenge (Proton Mail only)
    # if client.cookies.get('confirmation_code') == 'true':
    #     if not client.protonmail:
    #         print(f'[{RED}warning{RESET}] Please check your email for a confirmation code'
    #               f' and log in again using the web app. If you wish to automatically solve'
    #               f' email confirmation challenges, add a Proton Mail account in your account settings')
    #         return
    #     time.sleep(10)  # todo: just poll the inbox until it arrives instead of waiting
    #     client = solve_confirmation_challenge(client, *client.protonmail.values())

    return client


def login(email: str, username: str, password: str, **kwargs) -> Client:
    client = Client(
        cookies={
            "email": email,
            "username": username,
            "password": password,
            "guest_token": None,
            "flow_token": None,
        },
        headers={
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'en',
        })

    # client.protonmail = kwargs.get('protonmail')

    client = execute_login_flow(client)
    if kwargs.get('debug'):
        if not client or client.cookies.get('flow_errors') == 'true':
            print(f'[{RED}error{RESET}] {BOLD}{username}{RESET} login failed')
        else:
            print(f'[{GREEN}success{RESET}] {BOLD}{username}{RESET} login success')
    return client
