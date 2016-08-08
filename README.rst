jsonobject
==========

JSON serializable python3 objects.

Introduction
------------

The purpose with ``jsonobject`` is to provide a way to serialize and
deserialize python3 objects into and from JSON so that they can be communicated
with other application and stored into document databases such as CouchDB.

Some code and inspiration comes from the Django project, and the objects behave
much like such. However, while Django objects are meant for relational databases,
these are meant to be used with complex objects in document databases.

Dependencies
------------

There are no dependencies besides core python3.

Installation
------------

This repository can be installed with ``pip``.

Example
-------

.. code-block:: python

    from jsonobject import Property, PropertySet, EnumProperty

    class Wheel(PropertySet):
        diameter = Property(float, default=1.)

    class Rating(EnumProperty):
        ok = 'ok'
        bad = 'bad'
        good = 'good'

    class Car(PropertySet):
        wheels = Property(type=Wheel, is_list=True)
        brand = Property()
        model = Property()
        rating = Property(enum=Rating, default=Rating.ok)

    >>> volvo = Car(brand='Volvo', model='V70', rating=Rating.good)
    >>> volvo.to_json()
    '{\n  "*schema": "Car",\n  "brand": "Volvo",\n  "model": "V70",\n  "rating": "good",\n  "wheels": []\n}'
    >>> volvo.wheels.append(Wheel(diameter=2.))
    >>> volvo.to_json()
    '{\n  "*schema": "Car",\n  "brand": "Volvo",\n  "model": "V70",\n  "rating": "good",\n  "wheels": [\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    }\n  ]\n}'
    >>> volvo.wheels.append(Wheel(diameter=2.))
    >>> volvo.to_json()
    '{\n  "*schema": "Car",\n  "brand": "Volvo",\n  "model": "V70",\n  "rating": "good",\n  "wheels": [\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    }\n  ]\n}'
    >>> volvo.wheels.append(Wheel(diameter=2.))
    >>> volvo.wheels.append(Wheel(diameter=2.))
    >>> volvo.to_json()
    '{\n  "*schema": "Car",\n  "brand": "Volvo",\n  "model": "V70",\n  "rating": "good",\n  "wheels": [\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    }\n  ]\n}'
    >>> volvo2 = Car.FromJSON(volvo.to_json())
    >>> volvo2.to_json()
    '{\n  "*schema": "Car",\n  "brand": "Volvo",\n  "model": "V70",\n  "rating": "good",\n  "wheels": [\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    },\n    {\n      "*schema": "Wheel",\n      "diameter": 2.0\n    }\n  ]\n}'

Author
------

``jsonobject`` is written and maintained by Johan Egneblad <johan@egneblad>. 
