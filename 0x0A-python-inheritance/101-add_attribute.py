#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    if isinstance(obj, (list, dict, str, int, float, tuple)):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attribute, value)
