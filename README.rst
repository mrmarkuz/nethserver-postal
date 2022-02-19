=================
nethserver-postal
=================

Postal is a complete and fully featured mail server for use by websites & web servers.

Requirements
============

You need a dedicated virtualhost like postal.<DOMAIN>

Create admin user
==================

  postal make-user

Access
======

Access https://postal.<YOURDOMAIN>

Domain prop
===========

To use a custom domain you may set a VirtualHost:

  config setprop postal VirtualHost domain.tld
  signal-event nethserver-postal-update

Todos
=====

* backup
* postal systemd service
