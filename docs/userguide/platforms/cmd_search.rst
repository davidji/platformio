..  Copyright 2014-present Ivan Kravets <me@ikravets.com>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _cmd_platforms_search:

platformio platforms search
===========================

.. contents::

Usage
-----

.. code-block:: bash

    platformio platforms search QUERY [OPTIONS]


Description
-----------

Search for development :ref:`platforms`

Options
~~~~~~~

.. program:: platformio platforms search

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format


Examples
--------

1. Print all available development platforms

.. code-block:: bash

    $ platformio platforms search
    atmelavr (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    --------
    Atmel AVR 8- and 32-bit MCUs deliver a unique combination of performance...

    atmelsam (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    --------
    Atmel | SMART offers Flash- based ARM products based on the ...

    freescalekinetis (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ----------------
    Freescale Kinetis Microcontrollers is family of multiple hardware- and ...

    nordicnrf51 (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    -----------
    The Nordic nRF51 Series is a family of highly flexible, multi-protocol ...

    nxplpc (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ------
    The NXP LPC is a family of 32-bit microcontroller integrated circuits ...

    ststm32 (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    -------
    The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M ...

    teensy (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ------
    Teensy is a complete USB-based microcontroller development syste ...

    timsp430 (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    --------
    MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are ...

    titiva (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ------
    Texas Instruments TM4C12x MCUs offer the industrys most popular ...

2. Search for TI development platforms

.. code-block:: bash

    $ platformio platforms search ti
    timsp430 (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    --------
    MSP430 microcontrollers (MCUs) from Texas Instruments (TI) are ...

    titiva (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ------
    Texas Instruments TM4C12x MCUs offer the industrys most popular ...

3. Search for development platforms which support "mbed Framework"

.. code-block:: bash

    $ platformio platforms search mbed
    freescalekinetis (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ----------------
    Freescale Kinetis Microcontrollers is family of multiple hardware- and ...

    nordicnrf51 (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    -----------
    The Nordic nRF51 Series is a family of highly flexible, multi-protocol ...

    nxplpc (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    ------
    The NXP LPC is a family of 32-bit microcontroller integrated circuits ...

    ststm32 (available packages: ldscripts, toolchain-gccarmnoneeabi, tool-lm4flash, framework-opencm3, framework-energiativa)
    -------
    The STM32 family of 32-bit Flash MCUs based on the ARM Cortex-M ...
