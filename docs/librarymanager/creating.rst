..  Copyright 2014-2016 Ivan Kravets <me@ikravets.com>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _library_creating:
.. |PIOAPICR| replace:: *PlatformIO Library Registry Crawler*

Creating Library
================

*PlatformIO* :ref:`librarymanager` doesn't have any requirements to a library
source code structure. The only one requirement is library's manifest file -
:ref:`library_config`. It can be located inside your library or in the another
location where |PIOAPICR| will have *HTTP* access.

Updates to existing libraries are done every 24 hours. In case a more urgent
update is required, you can post a request on PlatformIO `community <https://community.platformio.org/>`_.

.. contents::

Source Code Location
--------------------

There are a several ways how to share your library with the whole world
(see `examples <https://github.com/platformio/platformio-libmirror/tree/master/configs>`_).

You can hold a lot of libraries (split into separated folders) inside one of
the repository/archive. In this case please use :ref:`libjson_include`
field to specify the relative path to your library's source code.


At GitHub
^^^^^^^^^

**Recommended**

If a library source code is located at `GitHub <https://github.com>`_, then
you **need to specify** only these fields in the :ref:`library_config`:

* :ref:`libjson_name`
* :ref:`libjson_keywords`
* :ref:`libjson_description`
* :ref:`libjson_repository`

|PIOAPICR| will populate the rest fields, like :ref:`libjson_version` or
:ref:`libjson_authors` with an actual information from *GitHub*.

Example:

.. code-block:: javascript

    {
        "name": "IRremote",
        "keywords": "infrared, ir, remote",
        "description": "Send and receive infrared signals with multiple protocols",
        "repository":
        {
            "type": "git",
            "url": "https://github.com/shirriff/Arduino-IRremote.git"
        },
        "frameworks": "arduino",
        "platforms": "atmelavr"
    }

Under CVS (SVN/GIT)
^^^^^^^^^^^^^^^^^^^

|PIOAPICR| can operate with a library source code that is under *CVS* control.
The list of **required** fields in the :ref:`library_config` will look like:

* :ref:`libjson_name`
* :ref:`libjson_keywords`
* :ref:`libjson_description`
* :ref:`libjson_authors`
* :ref:`libjson_repository`

Example:

.. code-block:: javascript

    {
        "name": "XBee",
        "keywords": "xbee, protocol, radio",
        "description": "Arduino library for communicating with XBees in API mode",
        "authors":
        {
            "name": "Andrew Rapp",
            "email": "andrew.rapp@gmail.com",
            "url": "https://code.google.com/u/andrew.rapp@gmail.com/"
        },
        "repository":
        {
            "type": "git",
            "url": "https://code.google.com/p/xbee-arduino/"
        },
        "frameworks": "arduino",
        "platforms": "atmelavr"
    }

Self-hosted
^^^^^^^^^^^

You can manually archive (*Zip, Tar.Gz*) your library source code and host it
in the *Internet*. Then you should specify the additional fields,
like :ref:`libjson_version` and :ref:`libjson_downloadurl`. The final list
of **required** fields in the :ref:`library_config` will look like:

* :ref:`libjson_name`
* :ref:`libjson_keywords`
* :ref:`libjson_description`
* :ref:`libjson_authors`
* :ref:`libjson_version`
* :ref:`libjson_downloadurl`

.. code-block:: javascript

    {
        "name": "OneWire",
        "keywords": "onewire, 1-wire, bus, sensor, temperature, ibutton",
        "description": "Control devices (from Dallas Semiconductor) that use the One Wire protocol (DS18S20, DS18B20, DS2408 and etc)",
        "authors":
        {
            "name": "Paul Stoffregen",
            "url": "http://www.pjrc.com/teensy/td_libs_OneWire.html"
        },
        "version": "2.2",
        "downloadUrl": "http://www.pjrc.com/teensy/arduino_libraries/OneWire.zip",
        "include": "OneWire",
        "frameworks": "arduino",
        "platforms": "atmelavr"
    }


Register
--------

The registration requirements:

* A library must adhere to the :ref:`library_config` specification.
* There must be public *HTTP* access to the library :ref:`library_config` file.

Now, you can :ref:`register <cmd_lib_register>` your library and allow others
to :ref:`install <cmd_lib_install>` it.


.. _library_creating_examples:

Examples
--------

Command:

.. code-block:: bash

    $ platformio lib register http://my.example.com/library.json

* `GitHub + fixed release <http://platformio.org/lib/show/552/ACNoblex>`_
* `Dependencies by author and framework <http://platformio.org/lib/show/3/PID-AutoTune>`_
* `Multiple libraries in the one repository <https://github.com/jrowberg/i2cdevlib/tree/master/Arduino>`_
