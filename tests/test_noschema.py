#!/usr/bin/env python3


from lindh.jsonobject import List, Dictionary
from lindh.jsonobject.noschema import merge_dicts


def test_dictionary_getattr():
    d = Dictionary()
    d['a'] = 123
    assert d.a == 123


def test_dictionary_where():
    d = Dictionary(a=1, b=2, c=3)
    w = d.where(lambda k, v: v >= 2)
    assert 'a' not in w
    assert 'b' in w
    assert 'c' in w


def test_dicrionary_dir():
    d = Dictionary(a=1, b=2, c=3)
    assert 'a' in dir(d)
    assert 'b' in dir(d)
    assert 'c' in dir(d)
    assert 'where' in dir(d)
    assert 'select' in dir(d)


def test_json_where_select():
    import io
    json_stream = io.StringIO('''
        {
            "data": [
                {"a": 1},
                {"a": 2},
                {"a": 3}
            ]
        }
    ''')
    d = Dictionary.load(json_stream)
    assert type(d.data) is List
    w = d.data.where(lambda x: x.a < 3).select(lambda x: x.a)
    assert 1 in w
    assert 2 in w
    assert 3 not in w


def test_merge_dicts():
    x = {'a': 1, 'b': 2, 'c': 3}
    y = {'c': 4, 'd': 5, 'e': 6}
    m = merge_dicts(x, y)
    assert m.a == 1
    assert m.b == 2
    assert m.c == 3
    assert m.c_ == 4
    assert m.d == 5
    assert m.e == 6


def test_extend():
    x = Dictionary(a=1, b=2, c=3)
    e = x.extend(d=4, e=5)
    assert e.a == 1
    assert e.b == 2
    assert e.c == 3
    assert e.d == 4
    assert e.e == 5


def test_join():
    import io
    json_stream = io.StringIO('''
        {
            "X": [
                {"id": 1, "a": 1},
                {"id": 1, "a": 2},
                {"id": 2, "a": 3},
                {"id": 2, "a": 4}
            ],
            "Y": [
                {"id": 1, "x_id": 2, "b": 1},
                {"id": 2, "x_id": 2, "b": 2},
                {"id": 3, "x_id": 1, "b": 3},
                {"id": 4, "x_id": 1, "b": 4}
            ]
        }
    ''')
    d = Dictionary.load(json_stream)
    j = d.X.where(lambda x: x.id == 1).join(d.Y, lambda x, y: x.id == y.x_id, lambda x, y: (x.a, y.b))
    assert (1, 3) in j
    assert (2, 4) in j
    assert (3, 1) not in j


def test_map_keys():
    d = Dictionary({"1": "a", "2": "b"})
    m = d.map_keys(int)
    assert 1 in m
    assert 2 in m
    assert m[1] == "a"
    assert m[2] == "b"


def test_change_list_and_reread():
    d = Dictionary({'a': [1, 2, 3]})
    d.a.append(4)
    assert len(d.a) == 4