ftw.oidcauth
============

A PAS plugin for authentication of users in Plone using OIDC.

Installation
------------

Make sure that `libxmlsec1-dev` and `libxml2-dev` are installed (the package
names are for Ubuntu and might differ slightly for other OS).

Then simply add the package to your instance eggs like:

```
[instance]
eggs +=
    ...
    ftw.oidcauth
```

Introduction
------------

The OIDC Plone PAS plugin can be added in `acl_users/manage_main`. After adding
a new Plugin it will be listed there and can be configured in detail.

OIDC Authorization Flow
***********************

1: Unauthorized User --------redirect--------> Authorization Endpoint
2: Callback View    <--------redirect--------  Authorization Endpoint
3: OIDC Plugin      <-------client call------> Token Endpoint
4: OIDC Plugin      <-------client call------> JWKS Endpoint
5: Validation of Token using the matching JWK
6: OIDC Plugin      <-------client call------> User Info Endpoint
7: Provision user in Plone

Configuration
*************

Once a plugin was added it can be configured by clicking on the plugin in
``acl_users/manage_main``.

Configuration: general configurations (oidc routes, secret...)
Users: manage users within this PAS plugin
Activate: select plugins implemented by the plugin


Links
-----

- Github: https://github.com/4teamwork/ftw.oidcauth
- Issues: https://github.com/4teamwork/ftw.oidcauth/issues


Copyright
---------

This package is copyright by `4teamwork <http://www.4teamwork.ch/>`_.

``ftw.oidcauth`` is licensed under GNU General Public License, version 2.
