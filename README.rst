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

.. code-block:: bash

    pip install https://github.com/eblade/jsonobject/archive/v1.0.tar.gz

Example
-------

.. testsetup:: *

    from jsonobject import Property, PropertySet, EnumProperty

.. testcode:: python

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

.. testcode::

    volvo = Car(brand='Volvo', model='V70', rating=Rating.good)
    print(volvo.to_json())

.. testoutput::

    {
        "*schema": "Car",
        "brand": "Volvo",
        "model": "V70",
        "rating": "good",
        "wheels": []
    }

.. testcode::

    volvo.wheels.append(Wheel(diameter=2.))
    print(volvo.to_json())

.. testoutput::

    {  
        "*schema": "Car",
        "brand": "Volvo",
        "model": "V70",
        "rating": "good",
        "wheels": [
            {
                "*schema": "Wheel",
                "diameter": 2.0
            }
        ]
    }

.. testcode::

    volvo.wheels.append(Wheel(diameter=2.))
    volvo.to_json()

.. testoutput::

    {
        "*schema": "Car",
        "brand": "Volvo",
        "model": "V70",
        "rating": "good",
        "wheels": [
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 2.0
            }
        ]
    }

.. testcode::

    volvo.wheels.append(Wheel(diameter=2.))
    volvo.wheels.append(Wheel())  # using default value here
    print(volvo.to_json())

.. testoutput::

    {
        "*schema": "Car",
        "brand": "Volvo",
        "model": "V70",
        "rating": "good",
        "wheels": [
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 1.0
            }
       ]
    }

.. testcode::

    volvo2 = Car.FromJSON(volvo.to_json())
    volvo2.to_json()

.. testoutput::

    {
        "*schema": "Car",
        "brand": "Volvo",
        "model": "V70",
        "rating": "good",
        "wheels": [
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 2.0
            },
            {
                "*schema": "Wheel",
                "diameter": 1.0
            }
        ]
    }


Author
------

``jsonobject`` is written and maintained by Johan Egneblad <johan@egneblad>. 
