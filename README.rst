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
    boot────────┬─╌╌╌╌╌╌╌╌agetty-tty2 ✔ ╌╌╌╌╌╌╌╌agetty-tty3 ✔ ╌╌╌╌╌╌╌╌agetty-tty4 ✔ 
                ├─╌╌╌╌╌╌╌╌agetty-tty5 ✔ ╌╌╌╌╌╌╌╌agetty-tty6 ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌binfmt ✔ 
                ├─╌╌╌╌╌╌╌╌╌╌╌╌cleanup ✔ ╌╌╌╌╌╌console-setup ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌╌dmesg ✔ 
                ├─╌╌╌╌╌╌╌╌╌╌╌hostname ✔ ╌╌╌╌╌╌╌╌╌╌╌╌hwclock ✔ ╌╌kmod-static-nodes ✔ 
                ├─╌╌╌╌╌╌╌╌╌╌╌╌modules ✔ ╌╌╌╌╌╌mount-cgroups ✔ ╌╌╌╌╌╌╌╌mount-devfs ✔ 
                ├─╌╌mount-filesystems ✔ ╌╌╌╌╌╌╌╌mount-sysfs ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌net-lo ✔ 
                ├─╌╌╌╌╌╌╌╌random-seed ✔ ╌╌╌╌╌╌╌╌╌╌╌rc-local ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌swap ✔ 
                ├─╌╌╌╌╌╌╌╌╌╌╌╌╌sysctl ✔ ╌╌╌╌╌╌╌╌╌╌╌╌sysuser ✔ ╌╌╌╌╌╌╌tmpfiles-dev ✔ 
                ├─╌╌╌╌╌tmpfiles-setup ✔ ╌╌╌╌╌╌╌╌╌╌╌╌udevadm ✔ ╌╌╌╌╌╌╌╌╌╌udevd-log ✔ 
                ╰─╌╌╌╌╌╌╌╌╌╌udevd-srv ✔ 
    connmand──────╌╌╌╌╌╌╌connmand-log ✘ ╌╌╌╌╌╌╌connmand-srv ✘ 
    dbus──────────╌╌╌╌╌╌╌╌╌╌╌dbus-log ✔ ╌╌╌╌╌╌╌╌╌╌╌dbus-srv ✔ 
    default─────┬─╌╌╌╌╌╌╌╌╌╌╌libvirtd ✔ ╌╌╌╌╌╌╌╌╌╌╌╌lightdm ✔ ╌╌╌╌╌╌╌╌lvmetad-srv ✔ 
                ╰─╌╌╌╌╌╌syslog-ng-log ✔ ╌╌╌╌╌╌syslog-ng-srv ✔ ╌╌╌╌╌╌╌╌╌╌╌virtlogd ✔ 
    elogind───────╌╌╌╌╌╌╌╌elogind-log ✘ ╌╌╌╌╌╌╌╌elogind-srv ✘ 
    getty───────┬─╌╌╌╌╌╌╌╌agetty-tty2 ✔ ╌╌╌╌╌╌╌╌agetty-tty3 ✔ ╌╌╌╌╌╌╌╌agetty-tty4 ✔ 
                ╰─╌╌╌╌╌╌╌╌agetty-tty5 ✔ ╌╌╌╌╌╌╌╌agetty-tty6 ✔ 
    lvmetad───────╌╌╌╌╌╌╌╌lvmetad-log ✔ ╌╌╌╌╌╌╌╌lvmetad-srv ✔ 
    misc────────┬─╌╌╌╌╌╌╌╌╌╌╌hostname ✔ ╌╌╌╌╌╌╌╌╌╌╌╌hwclock ✔ ╌╌kmod-static-nodes ✔ 
                ╰─╌╌╌╌╌╌╌╌╌╌╌╌modules ✔ ╌╌╌╌╌╌╌╌╌╌╌rc-local ✔ ╌╌╌╌╌╌╌tmpfiles-dev ✔ 
    mount───────┬─╌╌╌╌╌╌mount-cgroups ✔ ╌╌╌╌╌╌╌╌mount-devfs ✔ ╌╌mount-filesystems ✔ 
                ╰─╌╌╌╌╌╌╌╌mount-sysfs ✔ 
    NetworkManager╌NetworkManager-log ✔ ╌NetworkManager-srv ✔ 
    setup───────┬─╌╌╌╌╌╌╌╌agetty-tty2 ✔ ╌╌╌╌╌╌╌╌agetty-tty3 ✔ ╌╌╌╌╌╌╌╌agetty-tty4 ✔ 
                ├─╌╌╌╌╌╌╌╌agetty-tty5 ✔ ╌╌╌╌╌╌╌╌agetty-tty6 ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌binfmt ✔ 
                ├─╌╌╌╌╌╌╌╌╌╌╌╌cleanup ✔ ╌╌╌╌╌╌console-setup ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌╌dmesg ✔ 
                ├─╌╌╌╌╌╌╌╌╌╌╌╌╌net-lo ✔ ╌╌╌╌╌╌╌╌random-seed ✔ ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌swap ✔ 
                ╰─╌╌╌╌╌╌╌╌╌╌╌╌╌sysctl ✔ ╌╌╌╌╌╌╌╌╌╌╌╌sysuser ✔ ╌╌╌╌╌tmpfiles-setup ✔ 
    sshd──────────╌╌╌╌╌╌╌╌╌╌╌sshd-log ✘ ╌╌╌╌╌╌╌╌╌╌╌sshd-srv ✘ 
    syslog-ng─────╌╌╌╌╌╌syslog-ng-log ✔ ╌╌╌╌╌╌syslog-ng-srv ✔ 
    udev──────────╌╌╌╌╌╌╌╌╌╌╌╌udevadm ✔ ╌╌╌╌╌╌╌╌╌╌udevd-log ✔ ╌╌╌╌╌╌╌╌╌╌udevd-srv ✔ 
    udevd─────────╌╌╌╌╌╌╌╌╌╌udevd-log ✔ ╌╌╌╌╌╌╌╌╌╌udevd-srv ✔ 

List a few things::

    # service6 list default sshd sshd-log
    default╌╌╌╌╌╌libvirtd ✔ ╌╌╌╌╌╌╌lightdm ✔ ╌╌╌lvmetad-srv ✔ ╌syslog-ng-log ✔ 
         ╰─╌syslog-ng-srv ✔ ╌╌╌╌╌╌virtlogd ✔ 
    sshd───╌╌╌╌╌╌sshd-log ✘ ╌╌╌╌╌╌sshd-srv ✘ 
    ───────╌╌╌╌╌╌sshd-log ✘ 

List just a service::

    # service6 list sshd-log
    ╌sshd-log ✘ 

Start, stop, restart a service::

    # service6 list sshd
    sshd╌sshd-log ✘ ╌sshd-srv ✘ 
    # service6 start sshd
    >>> s6-rc -u -v 2 change sshd
    s6-rc: info: processing service sshd-log: starting
    s6-rc: info: service sshd-log started successfully
    s6-rc: info: processing service sshd-srv: starting
    s6-rc: info: service sshd-srv started successfully
    # service6 stop sshd
    >>> s6-rc -d -v 2 change sshd
    s6-rc: info: processing service sshd-srv: stopping
    s6-rc: info: service sshd-srv stopped successfully
    s6-rc: info: processing service sshd-log: stopping
    s6-rc: info: service sshd-log stopped successfully
    # service6 restart sshd
    >>> s6-rc -d -v 2 change sshd
    >>> s6-rc -u -v 2 change sshd
    s6-rc: info: processing service sshd-log: starting
    s6-rc: info: service sshd-log started successfully
    s6-rc: info: processing service sshd-srv: starting
    s6-rc: info: service sshd-srv started successfully
    # service6 list sshd   
    sshd╌sshd-log ✔ ╌sshd-srv ✔ 


Add and delete services from the default bundle (note that passing a bundle
deletes all its services, so maybe be careful)::

    # service6 list default
    default╌╌╌╌╌╌libvirtd ✔ ╌╌╌╌╌╌╌lightdm ✔ ╌╌╌lvmetad-srv ✔ ╌syslog-ng-log ✔ 
         ╰─╌syslog-ng-srv ✔ ╌╌╌╌╌╌virtlogd ✔ 
    # service6 add sshd    
    >>> s6-rc-bundle-update add default "sshd"
    # service6 list default
    default╌╌╌╌╌╌libvirtd ✔ ╌╌╌╌╌╌╌lightdm ✔ ╌╌╌lvmetad-srv ✔ ╌╌╌╌╌╌sshd-log ✔ 
         ╰─╌╌╌╌╌╌sshd-srv ✔ ╌syslog-ng-log ✔ ╌syslog-ng-srv ✔ ╌╌╌╌╌╌virtlogd ✔ 
    # service6 delete sshd 
    >>> s6-rc-bundle-update delete default "sshd-log sshd-srv"
    # service6 list default
    default╌╌╌╌╌╌libvirtd ✔ ╌╌╌╌╌╌╌lightdm ✔ ╌╌╌lvmetad-srv ✔ ╌syslog-ng-log ✔ 
         ╰─╌syslog-ng-srv ✔ ╌╌╌╌╌╌virtlogd ✔ 

The same but to a new bundle (note the error message below; it comes from
``s6-rc-bundle-update`` so maybe it'll go away one day, but I don't want to
suppress it through ``service6``)::

    # service6 list demo                
    ╌demo ❓
    # service6 add --bundle demo sshd
    >>> s6-rc-bundle add demo sshd
    # service6 list demo
    demo╌sshd-log ✔ ╌sshd-srv ✔ 
    # service6 delete --bundle demo sshd
    >>> s6-rc-bundle-update delete demo "sshd-log sshd-srv"
    s6-rc-bundle: usage: s6-rc-bundle [ -l live ] [ -c compiled ] [ -b ] command... (use s6-rc-bundle help for more information)
    # service6 list demo
    ╌demo ❓

Get help quickly on some bit of ``s6`` or ``sr-rc``::

    $ service6 help
    Available╌s6-accessrules-cdb-from-fs╌s6-accessrules-fs-from-cdb
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌s6-applyuidgid╌╌╌╌╌╌╌╌╌╌╌╌s6-cleanfifodir
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-connlimit╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-envdir
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-envuidgid╌╌╌╌╌╌╌╌╌s6-fdholder-daemon
           ├─╌╌╌╌╌╌╌╌╌s6-fdholder-delete╌╌╌╌╌s6-fdholder-errorcodes
           ├─╌╌╌╌╌╌╌╌s6-fdholder-getdump╌╌╌╌╌╌╌╌╌╌╌s6-fdholder-list
           ├─╌╌╌╌╌╌╌s6-fdholder-retrieve╌╌╌╌╌╌╌╌s6-fdholder-setdump
           ├─╌╌╌╌╌╌╌╌╌╌s6-fdholder-store╌╌╌s6-fdholder-transferdump
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-fdholderd╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-fghack
           ├─╌╌╌╌╌╌╌╌╌╌╌╌s6-ftrig-listen╌╌╌╌╌╌╌╌╌╌╌s6-ftrig-listen1
           ├─╌╌╌╌╌╌╌╌╌╌╌╌s6-ftrig-notify╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-ftrig-wait
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-ioconnect╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-ipcclient
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-ipcserver╌╌╌╌╌╌╌╌s6-ipcserver-access
           ├─╌╌s6-ipcserver-socketbinder╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-ipcserverd
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-log╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-mkfifodir
           ├─╌╌╌╌╌╌╌╌╌╌╌s6-notifyoncheck╌╌╌╌╌╌╌╌╌╌╌╌╌s6-permafailon
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc-bundle
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc-compile╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc-db
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc-dryrun╌╌╌╌╌╌s6-rc-fdholder-filler
           ├─╌╌╌╌╌╌╌s6-rc-format-upgrade╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc-init
           ├─╌╌╌╌╌╌╌╌╌╌s6-rc-oneshot-run╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-rc-update
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-setlock╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-setsid
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-setuidgid╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-softlimit
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-sudo╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-sudoc
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-sudod╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-supervise
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svc╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svdt
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svdt-clear╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svlisten
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svlisten1╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svok
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svscan╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svscan-1
           ├─╌╌╌╌╌╌╌╌╌╌╌╌s6-svscan-not-1╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svscanctl
           ├─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svstat╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-svwait
           ╰─╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌s6-tai64n╌╌╌╌╌╌╌╌╌╌╌╌╌s6-tai64nlocal
    You can access service6's help with --help/-h.
    $ PAGER=cat service6 help rc
    s6-rc
    Software
    skarnet.org
    The s6-rc program
    ...


