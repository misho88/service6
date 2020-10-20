service6
========

A wrapper around the service management parts of s6 (s6-rc, s6-rc-db,
s6-rc-bundle, s6-rc-bundle-update). Details: https://skarnet.org/software/s6-rc/

Why?
----

The utilities in s6-rc are very easy to script and not especially easy to type
out by hand, and the `-h` help isn't especially informative, so I had trouble
using the suite.

Current State
-------------

Feature complete, but likely a bit buggy, although I have been using it for months
without any issues. It can add/delete services from the database, start/stop/restart
services, list services and their current state, show logs of services, rebuild the
service database (on Artix), and show help on the s6 and s6-rc tools (pulled from
their git repos).

Installation
------------

The `python-argcomplete`, `python-natsort` and `python-blessed` are needed. Drop
the `python-` prefix if you wish to install them from PyPI.

Install w3c (to convert the s6/s6-rc documentation to text) and then install:

    $ make
    # make install

or just put the script somewhere in your path, but TAB-completion and reading of the
s6 documentation won't work.

s6-rc needs root permissions to get any information on services, and I didn't want to
make `service6` just call `sudo` (or `doas`) silently; therefore, to have 
TAB-completion work fully, export `SERVICE6_SUDO` or `SERVICE6_LIST_SUDO`.
With a password-prompt based `sudo`, I recommend::

    export SERVICE6_LIST_SUDO="sudo -n"
    export SERVICE6_SUDO="sudo"  # or just don't set it

Usage
-----

Read the help::

    $ service6 --help

List everything::

    # service6 list
    at───────────────────────────at-log ✔ ─────────────at-srv ✔ 
    boot──────────┬────────────────misc   ──────────────mount   ──────────────setup   
                  ╰────────────────udev   
    dbus───────────────────────dbus-log ✔ ───────────dbus-srv ✔ 
    default───────┬──────────────────at   ────────────elogind   ────────────lightdm   
                  ╰──────NetworkManager   ───────────────sshd   ─────────lm_sensors ✔ 
    ...

List a few things::

    # service6 list default sshd sshd-log
    default┬───────────────sshd   ────────────at-log ✔ ────────────at-srv ✔ ───────elogind-log ✔ 
           ├────────elogind-srv ✔ ───────lightdm-log ✔ ───────lightdm-srv ✔ ────────lm_sensors ✔ 
           ╰─NetworkManager-log ✔ NetworkManager-srv ✔ 
    sshd───────────────sshd-log ✔ ──────────sshd-srv ✔ 


List just a service::

    # service6 list sshd-log
    ──sshd-log ✔ 

Start, stop, restart a service::

    # service6 list sshd
    sshd──sshd-log ✘ sshd-srv ✘ 
    # service6 start sshd
    >>> s6-rc -u -v 2 change sshd
    s6-rc: info: service sshd-log: starting
    s6-rc: info: service sshd-log successfully started
    s6-rc: info: service sshd-srv: starting
    s6-rc: info: service sshd-srv successfully started
    # service6 stop sshd
    >>> s6-rc -d -v 2 change sshd
    s6-rc: info: service sshd-srv: stopping
    s6-rc: info: service sshd-srv successfully stopped
    s6-rc: info: service sshd-log: stopping
    s6-rc: info: service sshd-log successfully stopped
    # service6 restart sshd
    >>> s6-rc -d -v 2 change sshd
    >>> s6-rc -u -v 2 change sshd
    s6-rc: info: service sshd-log: starting
    s6-rc: info: service sshd-log successfully started
    s6-rc: info: service sshd-srv: starting
    s6-rc: info: service sshd-srv successfully started
    # service6 list sshd
    sshd──sshd-log ✔ sshd-srv ✔ 

Add and delete services from the default bundle (note that passing a bundle
deletes all its services, so maybe be careful)::

    # service6 list default
    default┬─────────────at-log ✔ ────────────at-srv ✔ ───────elogind-log ✔ ───────elogind-srv ✔ 
           ├────────lightdm-log ✔ ───────lightdm-srv ✔ ────────lm_sensors ✔ NetworkManager-log ✔ 
           ╰─NetworkManager-srv ✔ 
    # service6 add sshd    
    >>> s6-rc-bundle-update add default "sshd"
    # service6 list default
    default┬─────────────at-log ✔ ────────────at-srv ✔ ───────elogind-log ✔ ───────elogind-srv ✔ 
           ├────────lightdm-log ✔ ───────lightdm-srv ✔ ────────lm_sensors ✔ NetworkManager-log ✔ 
           ╰─NetworkManager-srv ✔ ──────────sshd-log ✔ ──────────sshd-srv ✔ 
    # service6 delete sshd 
    >>> s6-rc-bundle-update delete default "sshd-log sshd-srv"
    # service6 list default
    default┬─────────────at-log ✔ ────────────at-srv ✔ ───────elogind-log ✔ ───────elogind-srv ✔ 
           ├────────lightdm-log ✔ ───────lightdm-srv ✔ ────────lm_sensors ✔ NetworkManager-log ✔ 
           ╰─NetworkManager-srv ✔

The same but to a new bundle::

    # service6 list demo
    unknown───demo ⚠ 
    # service6 add --bundle demo sshd bluetoothd
    >>> s6-rc-bundle add demo sshd bluetoothd
    # service6 list demo
    demo───bluetoothd-log ✘ ─bluetoothd-srv ✘ ───────sshd-log ✔ ───────sshd-srv ✔ 
    # service6 delete --bundle demo sshd
    >>> s6-rc-bundle-update delete demo sshd-log sshd-srv
    # service6 delete --bundle demo bluetoothd
    >>> s6-rc-bundle delete demo
    # service6 list demo
    unknown───demo ⚠ 

Get help quickly on some bit of ``s6`` or ``sr-rc``::

    $ service6 help
    Available┬───────────────s6-svscanctl────────────s6-tai64nlocal─────────s6-rc-oneshot-run
             ├───────────────s6-softlimit───────────s6-ftrig-notify──────────────s6-ioconnect
            ...
             ╰─────────────s6-permafailon
    You can access service6's help with 'service6 --help/-h'.
    You can access each command's help with 'service6 command --help/-h'.
    $ PAGER=cat service6 help rc
    s6-rc
    Software
    skarnet.org
    The s6-rc program
    ...

Read a log (terrible choice of PAGER for demo only)::
    $ PAGER="head -3" service6 log sshd
    >>> head -3 /var/log/sshd/current
    2020-09-14 11:20:44.512831794  Server listening on 0.0.0.0 port 22.
    2020-09-14 11:20:44.512863490  Server listening on :: port 22.
    2020-09-26 21:54:23.214691224  Received signal 15; terminating.
