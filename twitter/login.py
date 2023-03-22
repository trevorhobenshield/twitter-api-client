import sys
from requests import Session
from .constants import SUCCESS, WARN, BOLD, RESET


def update_token(session: Session, key: str, url: str, payload: dict) -> Session:
    try:
        headers = {
            "authorization": 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            "content-type": "application/json",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            "x-guest-token": session.cookies.get('guest_token'),
            "x-csrf-token": session.cookies.get("ct0"),
            "x-twitter-auth-type": "OAuth2Session" if session.cookies.get("auth_token") else '',
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": 'en',
        }
        r = session.post(url, headers=headers, json=payload).json()
        session.cookies.set(key, r[key])
    except KeyError as e:
        print(f'[{WARN}FAILED{RESET}] failed to update token at {BOLD}{sys._getframe(1).f_code.co_name}{RESET}\n{e}')
    return session


def init_guest_token(session: Session) -> Session:
    return update_token(session, 'guest_token', 'https://api.twitter.com/1.1/guest/activate.json', {})


def flow_start(session: Session) -> Session:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json?flow_name=login', {
        "input_flow_data": {
            "flow_context": {"debug_overrides": {}, "start_location": {"location": "splash_screen"}}
        }, "subtask_versions": {}
    })


def flow_instrumentation(session: Session) -> Session:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', {
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginJsInstrumentationSubtask",
            "js_instrumentation": {"response": "{}", "link": "next_link"}
        }],
    })


def flow_username(session: Session) -> Session:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', {
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginEnterUserIdentifierSSO",
            "settings_list": {
                "setting_responses": [{
                    "key": "user_identifier",
                    "response_data": {"text_data": {"result": session.cookies.get('username')}}
                }], "link": "next_link"}}],
    })


def flow_password(session: Session) -> Session:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', {
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "LoginEnterPassword",
            "enter_password": {"password": session.cookies.get('password'), "link": "next_link"}}]
    })


def flow_duplication_check(session: Session) -> Session:
    return update_token(session, 'flow_token', 'https://api.twitter.com/1.1/onboarding/task.json', {
        "flow_token": session.cookies.get('flow_token'),
        "subtask_inputs": [{
            "subtask_id": "AccountDuplicationCheck",
            "check_logged_in_account": {"link": "AccountDuplicationCheck_false"},
        }],
    })


def execute_login_flow(session: Session) -> Session:
    session = init_guest_token(session)
    for fn in [flow_start, flow_instrumentation, flow_username, flow_password, flow_duplication_check]:
        session = fn(session)
    return session


def login(username: str, password: str) -> Session:
    session = Session()
    session.cookies.update({
        "username": username,
        "password": password,
        "guest_token": None,
        "flow_token": None,
    })
    session = execute_login_flow(session)
    print(f'[{SUCCESS}SUCCESS{RESET}] {BOLD}{username}{RESET} logged in successfully')
    return session
