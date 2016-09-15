# -*- coding: utf-8 -*-

from jsonobject import PropertySet, Property


def test_other_name():
    class O(PropertySet):
        id = Property(name='_id')

    o = O(id='myid')

    assert o.id == 'myid'


def test_other_name_to_dict():
    class O(PropertySet):
        id = Property(name='_id')

    o = O(id='myid')
    d = o.to_dict()

    assert d == {'*schema': 'O', '_id': 'myid'}
