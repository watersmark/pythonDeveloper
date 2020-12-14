import json
import functools


def to_json(func):

    @functools.wraps(func)
    def json_converter(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return json_converter
