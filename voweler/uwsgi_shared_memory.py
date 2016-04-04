# -*- coding: utf-8 -*-
"""
    uwsgi_shared_memory
    ~~~~~~~~~~~~~~~~~~~

    Module to manage state persistence across wsgi workers
"""
import json
import numpy as np
import uwsgi
from functools import partial


def get_state():
    """
    Deserializes JSON string saved in sharedarea index :memory_index
    """
    v = uwsgi.sharedarea_memoryview(0)
    data = v.tobytes()
    json_string = ''
    for char in data:
        char_ord = ord(char)
        if char_ord == 0:
            break
        else:
            json_string += char
    return json.loads(json_string)


def set_state(value):
    """
    Serializes object containing numpy arrays
    writes null bytes for remaining space in sharedarea
    """
    json_string = json.dumps(_prepare_numpy_object(value))
    memory_length = len(uwsgi.sharedarea_memoryview(0))
    uwsgi.sharedarea_write(0, 0, (
        json_string + (memory_length - len(json_string)) * b'\x00')
    )


def _prepare_numpy_object(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, dict):
        return {k: _prepare_numpy_object(v) for k, v in obj.iteritems()}
