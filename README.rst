=================
nethserver-postal
=================

Postal is a complete and fully featured mail server for use by websites & web servers.

Requirements
============

* You need a dedicated virtualhost like postal.<DOMAIN>
* Nethserver-postal uses postal.<NETHSERVERDOMAIN> by default.

Domain prop
===========

To use a custom domain like postal.<CUSTOMDOMAIN> you may set the VirtualHost prop:

  config setprop postal VirtualHost domain.tld

Apply config

  signal-event nethserver-postal-update

Create admin user
==================

To create an admin user execute

  postal make-user

Access
======

Access postal via https://postal.<YOURDOMAIN>

Todos
=====

* backup - backup volumes or db
* create services for opening firewall
* set ports in config files from services
