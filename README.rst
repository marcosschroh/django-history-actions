=============================
django-history-actions
=============================

.. image:: https://badge.fury.io/py/django-history-actions.svg
    :target: https://badge.fury.io/py/django-history-actions

.. image:: https://travis-ci.org/marcosschroh/django-history-actions.svg?branch=master
    :target: https://travis-ci.org/marcosschroh/django-history-actions

.. image:: https://codecov.io/gh/marcosschroh/django-history-actions/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/marcosschroh/django-history-actions

This Project is in PROGRESS
---------------------------

Django app to track actions/events accros systems.

Documentation
-------------

The full documentation is at https://django-history-actions.readthedocs.io.

Quickstart
----------

Install django-history-actions::

    pip install django-history-actions

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'history_actions.apps.HistoryActionsConfig',
        ...
    )

Add django-history-actions's URL patterns:

.. code-block:: python

    from history_actions import urls as history_actions_urls


    urlpatterns = [
        ...
        url(r'^', include(history_actions_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
