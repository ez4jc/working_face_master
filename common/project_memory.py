# !/usr/bin/python
# -*- coding: utf-8 -*-

def initialize():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defValue=None):
    try:
        if name in _global_dict:
            return _global_dict[name]
    except KeyError:
        return defValue
