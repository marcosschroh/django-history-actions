=====
Usage
=====

To use django-history-actions in a project, add it to your `INSTALLED_APPS`:

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
