# -*- coding: utf-8 -*-

from jsonobject import PropertySet, Property


def test_other_name():
    class O(PropertySet):
        id = Property(name='_id')

    o = O(id='myid')

    assert o.id == 'myid'
