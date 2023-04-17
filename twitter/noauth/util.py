import logging.config
import time
from pathlib import Path

import orjson

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
ERROR = '\u001b[31m'
WARN = '\u001b[33m'
RESET = '\u001b[0m'

log_config = {
    "version": 1,
    "formatters": {
        "simple": {
            "format": "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "simple",
            "filename": "debug.log",
            "encoding": "utf8",
            "mode": "a"
        }
    },
    "loggers": {
        "myLogger": {
            "level": "DEBUG",
            "handlers": [
                "console"
            ],
            "propagate": "no"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "file"
        ]
    }
}

logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)


def find_key(obj: any, key: str) -> list:
    """
    Find all values of a given key within a nested dict or list of dicts

    @param obj: dictionary or list of dictionaries
    @param key: key to search for
    @return: list of values
    """

    def helper(obj: any, key: str, L: list) -> list:
        if not obj:
            return L

        if isinstance(obj, list):
            for e in obj:
                L.extend(helper(e, key, []))
            return L

        if isinstance(obj, dict) and obj.get(key):
            L.append(obj[key])

        if isinstance(obj, dict) and obj:
            for k in obj:
                L.extend(helper(obj[k], key, []))
        return L

    return helper(obj, key, [])


def get_cursor(data: list | dict) -> str:
    # inefficient, but need to deal with arbitrary schema
    entries = find_key(data, 'entries')
    if entries:
        for entry in entries.pop():
            entry_id = entry.get('entryId', '')
            if ('cursor-bottom' in entry_id) or ('cursor-showmorethreads' in entry_id):
                content = entry['content']
                if itemContent := content.get('itemContent'):
                    return itemContent['value']  # v2 cursor
                return content['value']  # v1 cursor


def save_data(data: list, op: tuple, key: str | int):
    try:
        path = Path(f'data/raw/{key}')
        path.mkdir(parents=True, exist_ok=True)
        (path / f'{time.time_ns()}_{op}.json').write_text(
            orjson.dumps(data, option=orjson.OPT_INDENT_2).decode(),
            encoding='utf-8'
        )
    except Exception as e:
        logger.debug(f'[{ERROR}error{RESET}] failed to save data: {e}')
