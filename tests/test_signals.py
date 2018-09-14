# -*- coding: utf-8 -*-
from mock import patch

from django.test import TestCase
# from django.conf import settings

from django.contrib.auth.models import User

# from history_actions.models import HistoryActions
# from history_actions.history_manager import HistoryManager
# from tests.app_test import models
from tests.app_test.actions import PROFILE_SAVE_ACTION


class TestHistorySignals(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('username', 'username@gmail.com',
                                             'username')

    @patch(
        'history_actions.history_manager.HistoryManager.check_existing_action',
        return_value=PROFILE_SAVE_ACTION)
    def test_create_history_from_signal(self, check_existing_action_fn):
        pass
