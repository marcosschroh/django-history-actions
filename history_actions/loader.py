from django.apps import apps
from django.db.models.signals import post_save

from history_actions.base import SaveHistory


def subscribe_to_signals():
    for app, models in apps.all_models.items():
        for model_name, model in models.items():
            bases = [klase_base.__name__ for klase_base in model.__bases__]

            if 'SaveHistory' in bases:
                post_save.connect(SaveHistory.save_signal_callback, sender=model)
