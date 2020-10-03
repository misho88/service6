service6
========

A wrapper around the service management parts of s6 (s6-rc, s6-rc-db,
s6-rc-bundle, s6-rc-bundle-update). Details: https://skarnet.org/software/s6/

Why?
----

s6's tools really look like they're more meant to be scripted than used by
humans. This isn't a bad thing. It has certainly made writing this utility
very easy and I wish more software suites were written with that kind of 
granularity; however, remembering those commands and typing them over and
over again is an absolute chore.

Current State
-------------

I wrote this in a few hours over the weekend, so not great, but I think it's
usable. The main feature missing is a way to read logs. Some documentation is
also in order.

Installation
------------

Install w3c and then install::

    # make install

Or just put the script somewhere in your path (but ``service6 help`` won't
work, which is probably fine).

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

The same but to a new bundle (note the error message below; it comes from
``s6-rc-bundle-update`` so maybe it'll go away one day, but I don't want to
suppress it through ``service6``)::

    # service6 list demo
    unknown──demo ❓
    # service6 add --bundle demo sshd
    >>> s6-rc-bundle add demo sshd
    # service6 list demo
    demo──sshd-log ✔ sshd-srv ✔ 
    # service6 delete --bundle demo sshd
    >>> s6-rc-bundle-update delete demo "sshd-log sshd-srv"
    s6-rc-bundle: usage: s6-rc-bundle [ -l live ] [ -c compiled ] [ -b ] command... (use s6-rc-bundle help for more information)
    Command '['s6-rc-bundle-update', 'delete', 'demo', 'sshd-log sshd-srv']' returned non-zero exit status 100.
    # service6 list demo
    unknown──demo ❓

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


