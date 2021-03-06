from django.db import models
import uuid

from django.conf import settings

from history_actions.history_manager import HistoryManager
from history_actions import mixins
from tests.app_test.actions import PROFILE_SAVE_ACTION


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='user',
        related_name='profiles',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.user, self.uuid)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        HistoryManager.create(
            'admin',
            PROFILE_SAVE_ACTION,
            model_instance=self
        )

    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "user": self.user.username
        }


class ProfilePostSaveSignal(models.Model, mixins.PostSaveHistory):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)


class SuperProfile(models.Model):
    HISTORY_ACTIONS_SYSTEM = 'chat'

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uuid)

    def save(self, *args, **kwargs):
        super(SuperProfile, self).save(*args, **kwargs)

        HistoryManager.create(
            'admin',
            PROFILE_SAVE_ACTION,
            model_instance=self
        )
