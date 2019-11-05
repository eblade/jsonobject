import pytest
from lindh.jsonobject import Property, PropertySet, EnumProperty


def test_using_non_enum_enum_for_enum_value():
    class E(EnumProperty):
        a = 1

    class A(PropertySet):
        a = Property(enum=E, default=E.a)

    a = A()
    with pytest.raises(ValueError):
        a.a = 'blerg'


def test_is_embedded():
    class A(PropertySet):
        pass

    class B(PropertySet):
        a: A = Property()

    assert B.a.is_embedded


def test_is_not_embedded():
    class A(PropertySet):
        a: int = Property()

    assert not A.a.is_embedded
