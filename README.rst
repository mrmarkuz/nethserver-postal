=================
nethserver-postal
=================

Postal is a complete and fully featured mail server for use by websites & web servers.

Requirements
============

* You need a dedicated virtualhost like postal.<DOMAIN>
* Nethserver-postal uses postal.<NETHSERVERDOMAIN> by default.

Set Domain
==========

To use a custom domain like postal.<CUSTOMDOMAIN> you may set the VirtualHost prop:

  config setprop postal VirtualHost domain.tld

Set subdomain
=============

To use a custom subdomain instead of postal you may set the subdomain prop to get mysub.domain.tld instead of postal.domain.tld:

  config setprop postal subdomain mysub

Set mail user and mail password
===============================

After configuring a mail server, user and password you need to set it for the web management to be able to send mails:

  config setprop postal mailuser user@sub.domain.tld
  config setprop postal mailpass secretpassword

Apply configuration after changes
=================================

Apply config by executing

  signal-event nethserver-postal-update

Create admin user
==================

To create an admin user execute

  postal make-user

Access
======

Access postal via https://<YOURSUBDOMAIN>.<YOURDOMAIN> like https://postal.domain.tld
