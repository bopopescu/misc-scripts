Changelog
=========

0.5.0 (Jun 16, 2015)
^^^^^^^^^^^^^^^^^^^^

- Write access to the input device is no longer mandatory. Evdev will
  first try to open the device for reading and writing and fallback to
  read-only. Methods that require write access (e.g. ``set_led()``)
  will raise ``EvdevError`` if the device is open only for reading.

0.4.7 (Oct 07, 2014)
^^^^^^^^^^^^^^^^^^^^

- Fallback to distutils if setuptools is not available.

0.4.6 (Oct 07, 2014)
^^^^^^^^^^^^^^^^^^^^

- Rework documentation and docstrings once more.

- Fix install on Python 3.4 (works around issue21121_).

- Fix ``ioctl()`` requested buffer size (thanks Jakub Wojciech Klama).

0.4.5 (Jul 06, 2014)
^^^^^^^^^^^^^^^^^^^^

- Add method for returning a list of the currently active keys -
  ``InputDevice.active_keys()`` (thanks `@spasche`_).

- Fix a potential buffer overflow in ``ioctl_capabilities`` (thanks `@spasche`_).

0.4.4 (Jun 04, 2014)
^^^^^^^^^^^^^^^^^^^^

- Calling ``InputDevice.read_one()`` should always return ``None``,
  when there is nothing to be read, even in case of a ``EAGAIN`` errno
  (thanks JPP).

0.4.3 (Dec 19, 2013)
^^^^^^^^^^^^^^^^^^^^
- Silence ``OSError`` in destructor (thanks `@polyphemus`_).

- Make ``InputDevice.close()`` work in cases in which stdin (fd 0) has
  been closed (thanks `@polyphemus`_).

0.4.2 (Dec 13, 2013)
^^^^^^^^^^^^^^^^^^^^

- Rework documentation and docstrings.

- Call ``InputDevice.close()`` from ``InputDevice.__del__()``.

0.4.1 (Jul 24, 2013)
^^^^^^^^^^^^^^^^^^^^

- Fix reference counting in ``device_read``, ``device_read_many`` and
  ``ioctl_capabilities``.

0.4.0 (Jul 01, 2013)
^^^^^^^^^^^^^^^^^^^^

- Add ``FF_*`` and ``FF_STATUS`` codes to ``ecodes`` (thanks `@bgilbert`_).

- Reverse event code mappings (``ecodes.{KEY,FF,REL,ABS}`` and etc.)
  will now map to a list of codes, whenever a value corresponds to
  multiple codes::

    >>> ecodes.KEY[152]
    ... ['KEY_COFFEE', 'KEY_SCREENLOCK']
    >>> ecodes.KEY[30]
    ... 'KEY_A'

- Set the state of a LED through ``device.set_led()`` (thanks
  `@accek`_). ``device.fd`` is opened in ``O_RDWR`` mode from now on.

- Fix segfault in ``device_read_many()`` (thanks `@bgilbert`_).

0.3.3 (May 29, 2013)
^^^^^^^^^^^^^^^^^^^^

- Raise ``IOError`` from ``device_read()`` and ``device_read_many()`` when
  ``read()`` fails.

- Several stability and style changes (thank you debian code reviewers).

0.3.2 (Apr 05, 2013)
^^^^^^^^^^^^^^^^^^^^

- Fix vendor id and product id order in ``DeviceInfo`` (thanks `@kived`_).

0.3.1 (Nov 23, 2012)
^^^^^^^^^^^^^^^^^^^^

- ``device.read()`` will return an empty tuple if the device has
  nothing to offer (instead of segfaulting).

- Exclude unnecessary package data in sdist and bdist.

0.3.0 (Nov 06, 2012)
^^^^^^^^^^^^^^^^^^^^

- Add ability to set/get auto-repeat settings with ``EVIOC{SG}REP``.

- Add ``device.version`` - the value of ``EVIOCGVERSION``.

- Add ``device.read_loop()``.

- Add ``device.grab()`` and ``device.ungrab()`` - exposes ``EVIOCGRAB``.

- Add ``device.leds`` - exposes ``EVIOCGLED``.

- Replace ``DeviceInfo`` class with a namedtuple.

- Prevent ``device.read_one()`` from skipping events.

- Rename ``AbsData`` to ``AbsInfo`` (as in ``struct input_absinfo``).


0.2.0 (Aug 22, 2012)
^^^^^^^^^^^^^^^^^^^^

- Add the ability to set arbitrary device capabilities on uinput
  devices (defaults to all ``EV_KEY`` ecodes).

- Add ``UInput.device`` which is an open ``InputDevice`` to the
  input device that uinput 'spawns'.

- Add ``UInput.capabilities()`` which is just a shortcut to
  ``UInput.device.capabilities()``.

- Rename ``UInput.write()`` to ``UInput.write_event()``.

- Add a simpler ``UInput.write(type, code, value)`` method.

- Make all ``UInput`` constructor arguments optional (default
  device name is now ``py-evdev-uinput``).

- Add the ability to set ``absmin``, ``absmax``, ``absfuzz`` and
  ``absflat`` when specifying the uinput device's capabilities.

- Remove the ``nophys`` argument - if a device fails the
  ``EVIOCGPHYS`` ioctl, phys will equal the empty string.

- Make ``InputDevice.capabilities()`` perform a ``EVIOCGABS`` ioctl
  for devices that support ``EV_ABS`` and return that info wrapped in
  an ``AbsData`` namedtuple.

- Split ``ioctl_devinfo`` into ``ioctl_devinfo`` and
  ``ioctl_capabilities``.

- Split ``uinput_open()`` to ``uinput_open()`` and ``uinput_create()``

- Add more uinput usage examples and documentation.

- Rewrite uinput tests.

- Remove ``mouserel`` and ``mouseabs`` from ``UInput``.

- Tie the sphinx version and release to the distutils version.

- Set 'methods-before-attributes' sorting in the docs.

- Remove ``KEY_CNT`` and ``KEY_MAX`` from ``ecodes.keys``.


0.1.1 (May 18, 2012)
^^^^^^^^^^^^^^^^^^^^

- Add ``events.keys``, which is a combination of all ``BTN_`` and
  ``KEY_`` event codes.

- ``ecodes.c`` was not generated when installing through ``pip``.


0.1.0 (May 17, 2012)
^^^^^^^^^^^^^^^^^^^^

*Initial Release*

.. _`@polyphemus`: https://github.com/polyphemus
.. _`@bgilbert`: https://github.com/bgilbert
.. _`@accek`: https://github.com/accek
.. _`@kived`: https://github.com/kived
.. _`@spasche`: https://github.com/spasche

.. _issue21121: http://bugs.python.org/issue21121
