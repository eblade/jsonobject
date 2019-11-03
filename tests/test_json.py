from lindh.jsonobject import PropertySet, Property


def test_json_1():
    class O(PropertySet):
        a = Property(str)
        b = Property(int)
        c = Property(float)
        d = Property(bool)
        e = Property(list)

    o = O(
        a='test',
        b=42,
        c=42.3,
        d=True,
        e=[1, 'string', False],
    )

    assert o.to_dict() == O(o.to_dict()).to_dict()
    assert o.to_json() == O.FromJSON(o.to_json()).to_json()


def test_json_2():
    class P(PropertySet):
        a = Property(int)

    class O(PropertySet):
        a = Property(str)
        b = Property(int)
        c = Property(float)
        d = Property(bool)
        e = Property(list)
        f = Property(P)

    o = O(
        a='test',
        b=42,
        c=42.3,
        d=True,
        e=[1, 'string', False],
        f=P(a=45),
    )

    assert o.to_dict() == O(o.to_dict()).to_dict()
    assert o.to_json() == O.FromJSON(o.to_json()).to_json()


def test_json_3():
    class P(PropertySet):
        a = Property(int)

    class O(PropertySet):
        a = Property(str)
        b = Property(int)
        c = Property(float)
        d = Property(bool)
        e = Property(list)
        f = Property(P, is_list=True)

    o = O(
        a='test',
        b=42,
        c=42.3,
        d=True,
        e=[1, 'string', False],
        f=[P(a=45)],
    )

    assert o.to_dict() == O(o.to_dict()).to_dict()
    assert o.to_json() == O.FromJSON(o.to_json()).to_json()


def test_json_4():
    class P(PropertySet):
        a = Property(int)

    class O(PropertySet):
        d = Property(dict)

    o = O()

    assert o.to_dict().get('d') == {}
    assert o.to_dict() == O(o.to_dict()).to_dict()
    assert o.to_json() == O.FromJSON(o.to_json()).to_json()


def test_if_string_is_passed_to_sub_propertyset_it_should_be_parsed():
    class P(PropertySet):
        a: int = Property()

    class Q(PropertySet):
        p: P = Property()

    q = Q()
    q.p = '{"a": 42}'
    assert q.p.a == 42
