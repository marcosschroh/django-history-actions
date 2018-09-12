from django.apps import apps
from django.db.models.signals import post_save

from history_actions import mixins


def subscribe_to_signals():
    for app, models in apps.all_models.items():
        for _, model in models.items():

            if issubclass(model, mixins.PostSaveHistory):
                post_save.connect(
                    mixins.PostSaveHistory.save_signal_callback, sender=model)
