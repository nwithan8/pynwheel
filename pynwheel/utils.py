import time
from enum import Enum


def replace_enums(**kwargs):
    """
    No support for lists right now
    :param kwargs:
    :type kwargs:
    :return:
    :rtype:
    """
    cleaned_kwargs = {}
    for k, v in kwargs.items():
        if v is None:
            pass
        elif Enum in v.__bases__:
            cleaned_kwargs[k] = v.name
        else:
            cleaned_kwargs[k] = v
    return cleaned_kwargs


def timestamp_is_expired(timestamp: str):
    try:
        timestamp = int(timestamp)
        current_timestamp = int(time.time())
        return timestamp < current_timestamp
    except:
        raise Exception("Could not check timestamp expiration.")
