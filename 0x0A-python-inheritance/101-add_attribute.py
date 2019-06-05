#!/usr/bin/python3
def add_attribute(obj, attribute, value):
    if '__dict__' not in dir(obj) or '__slots__' in dir(obj):
        raise TypeError('can\'t add new attribute')
    setattr(obj, attribute, value)
