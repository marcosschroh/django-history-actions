# -*- coding: utf-8
from django.apps import AppConfig
from history_actions import loader


class HistoryActionsConfig(AppConfig):
    name = 'history_actions'

    def ready(self):
        loader.subscribe_to_signals()
