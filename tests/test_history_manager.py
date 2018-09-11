# -*- coding: utf-8 -*-
from mock import patch

from django.test import TestCase
from django.conf import settings

from django.contrib.auth.models import User

from history_actions.models import HistoryActions
from history_actions.manager import HistoryManager
from tests.app_test.models import Profile, SuperProfile
from tests.app_test.actions import PROFILE_SAVE_ACTION


class TestHistoryManager(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'username',
            'username@gmail.com',
            'username'
        )
        self.profile_content_type = Profile()._meta.label
        self.superprofile_content_type = SuperProfile()._meta.label

    @patch('history_actions.manager.HistoryManager.check_existing_action', return_value=PROFILE_SAVE_ACTION)
    def test_create_history(self, check_existing_action_fn):
        profile = Profile.objects.create(user=self.user)
        check_existing_action_fn.assert_called_once_with(PROFILE_SAVE_ACTION, profile)

        self.assertTrue(
            HistoryActions.objects.get(
                author='admin',
                action=PROFILE_SAVE_ACTION,
                system=settings.HISTORY_ACTIONS_SYSTEM,
                object_pk=profile.pk,
                content_type=self.profile_content_type
            )
        )

    @patch('history_actions.manager.HistoryManager.check_existing_action', return_value=PROFILE_SAVE_ACTION)
    def test_create_history_extra_fields(self, check_existing_action_fn):
        profile = Profile.objects.create(user=self.user)
        notes = 'extra notes..'

        HistoryManager.create(
            'admin',
            PROFILE_SAVE_ACTION,
            model_instance=profile,
            extra=profile.to_dict(),
            notes=notes
        )

        check_existing_action_fn.assert_called_with(PROFILE_SAVE_ACTION, profile)

        self.assertTrue(
            HistoryActions.objects.get(
                author='admin',
                action=PROFILE_SAVE_ACTION,
                system=settings.HISTORY_ACTIONS_SYSTEM,
                object_pk=profile.pk,
                content_type=self.profile_content_type,
                notes=notes,
                extra__isnull=False
            )
        )

    @patch('history_actions.manager.HistoryManager.check_existing_action', return_value=PROFILE_SAVE_ACTION)
    def test_create_history_custom_system_name(self, check_existing_action_fn):
        profile = SuperProfile.objects.create()
        check_existing_action_fn.assert_called_once_with(PROFILE_SAVE_ACTION, profile)

        self.assertTrue(
            HistoryActions.objects.get(
                author='admin',
                action=PROFILE_SAVE_ACTION,
                system='chat',
                object_pk=profile.pk,
                content_type=self.superprofile_content_type
            )
        )

    def test_create_history_from_signal(self):
        pass

    def test_actions_file_does_not_exist(self):
        """
        Because there is not a module called actions.py in auth app,
        it raise an ImportError
        """
        with self.assertRaises(ImportError):
            HistoryManager.create(
                'admin',
                PROFILE_SAVE_ACTION,
                model_instance=self.user
            )

    @patch('history_actions.manager.HistoryManager.check_existing_action', return_value={'ACTIONS': {}})
    def test_action_does_not_exist(self, get_actions_fn):
        profile = Profile()

        with self.assertRaises(Exception):
            HistoryActions.check_existing_action('some action', profile)
