import copy
from importlib import import_module
from future.utils import raise_from

from django.conf import settings

from history_actions.models import HistoryActions


class HistoryManager:

    # Class attribute to cache the actions from actions.py
    ACTIONS = {}

    @staticmethod
    def get_actions(app_label):
        try:
            return import_module('.actions', app_label)
        except ImportError as exc:
            raise raise_from(
                ImportError('actions.py file does not exist in app {0}'.format(app_label)), exc)

    @classmethod
    def check_existing_action(cls, action, model_instance):
        """
        Check whether the action exist in action.py file
        """
        app_label = model_instance._meta.app_label

        if app_label not in cls.ACTIONS:
            actions_module = cls.get_actions(app_label)

            if not actions_module.ACTIONS.get(action):
                raise Exception(
                    'Action {0} does not exist in actions.py file for app {1}'.format(action, app_label))

            # cache the actions
            cls.ACTIONS[app_label] = copy.deepcopy(actions_module.ACTIONS)
        else:
            cls.ACTIONS[app_label][action]

    @classmethod
    def create(cls, author, action, **kwargs):
        model_instance = kwargs.pop('model_instance', None)

        # this is the priority 1
        system = kwargs.pop('system', None)

        if not kwargs.pop('from_signal', None) and model_instance:
            cls.check_existing_action(action, model_instance)

        if model_instance:
            kwargs['content_type'] = model_instance._meta.label
            kwargs['object_pk'] = model_instance.pk

            system_from_model = getattr(model_instance, 'HISTORY_ACTIONS_SYSTEM', None)
            if not system and system_from_model:
                system = system_from_model

        system = system or settings.HISTORY_ACTIONS_SYSTEM

        HistoryActions.create(author, action, system, **kwargs)

    @classmethod
    def get_history(cls):
        pass
