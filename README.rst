|license|

:Version: 0.0.0
:Web: https://github.com/luismayta/pyfacebook
:Download: https://github.com/luismayta/pyfacebook
:Source: https://github.com/luismayta/pyfacebook
:Keywords: pyfacebook

.. contents:: Table of Contents:
    :local:

PyFacebook
==========

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.rst`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute`_ for details.

PR description template should be automatically applied if you are sending PR from gitlab interface; otherwise you
can find it it at `PULL_REQUEST_TEMPLATE`_

Issue report template should be automatically applied if you are sending it from gitlab UI as well; otherwise you
can find it at `ISSUE_TEMPLATE`_

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@luismayta.com.

Requirements
------------

This is a list of applications that need to be installed previously to
enjoy all the goodies of this configuration:

-  `Pyenv`_
-  `Terraform`_
-  `Terragrunt`_
-  `Docker`_
-  `Docker Compose`_

.. code:: bash

    $ make setup
    $ make docker.build service=app

Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog


Troubleshooting
---------------

Wrong pre-commit with pyenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute the next:

.. code:: bash

    pyenv shell 3.7.3


License
=======

GNU

Changelog
---------

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
============

Please see `CONTRIBUTING`_ for details.


Versioning
----------

Releases are managed using bitbucket release feature. We use [Semantic Versioning](http://semver.org) for all
the releases. Every change made to the code base will be referred to in the release notes (except for
cleanups and refactorings).

Credits
-------

-  `CONTRIBUTORS`_

Made with :heart: :coffee: and :pizza: by `company`_.

.. |license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
  :target: LICENSE
  :alt: License

.. Links
.. _`CHANGELOG`: CHANGELOG.rst
.. _`RELEASING`: docs/source/RELEASING.rst
.. _`TESTING`: docs/source/TESTING.rst
.. _`CONTRIBUTORS`: docs/source/AUTHORS.rst
.. _`CONTRIBUTING`: docs/source/CONTRIBUTING.rst
.. _`TROUBLESHOOTING`: docs/source/TROUBLESHOOTING.rst

.. _`PULL_REQUEST_TEMPLATE`: .bitbucket/pull_request_templates/PULL_REQUEST_TEMPLATE.md
.. _`ISSUE_TEMPLATE`: .bitbucket/issue_templates/ISSUE_TEMPLATE.md

.. _`How To Contribute`: docs/source/CONTRIBUTING.rst


.. _`company`: https://github.com/luismayta
.. dependences
.. _`Pyenv`: https://github.com/pyenv/pyenv
.. _`Docker`: https://www.docker.com/
.. _`Docker Compose`: https://docs.docker.com/compose/
.. _`Terraform`: https://www.terraform.io
.. _`Terragrunt`: https://github.com/gruntwork-io/terragrunt
