# -*- coding: utf-8 -*-

import pytest
from jsonobject import PropertySet, Property, EnumProperty


def test_set_via_contructor():
    class O(PropertySet):
        s = Property()

    o = O(s='test')

    assert o.s == 'test'


def test_set_via_attribute():
    class O(PropertySet):
        s = Property()

    o = O()
    o.s = 'test'

    assert o.s == 'test'


def test_set_default():
    class O(PropertySet):
        s = Property(default='test')

    o = O()

    assert o.s == 'test'


def test_set_required_missing():
    class O(PropertySet):
        s = Property(required=True)

    with pytest.raises(ValueError):
        o = O(s=None)

    with pytest.raises(ValueError):
        o = O(s='test')
        o.s = None 


def test_set_required_present():
    class O(PropertySet):
        s = Property(required=True)

    o = O(s='test')


def test_none_by_kwarg():
    class O(PropertySet):
        s = Property(none='-')
    
    o = O(s=None)

    assert o.s == '-'


def test_none_by_default():
    class O(PropertySet):
        s = Property(none='-')
    
    o = O()

    assert o.s == '-'


def test_none_by_explicit_default():
    class O(PropertySet):
        s = Property(default=None, none='-')
    
    o = O()

    assert o.s == '-'


def test_none_by_attribute():
    class O(PropertySet):
        s = Property(none='-')
    
    o = O()
    o.s = None

    assert o.s == '-'


def test_external_validator():
    def validator(value):
        if value == 'wrong':
            raise ValueError

    class O(PropertySet):
        s = Property(validator=validator)
    
    o = O(s='right')

    with pytest.raises(ValueError):
        o.s = 'wrong'

