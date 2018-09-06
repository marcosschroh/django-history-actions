# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models

from model_utils.models import TimeStampedModel


class HistoryActions(TimeStampedModel):
    author = models.CharField(max_length=64, help_text='Author of the action. Is username or System.')
    actor = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        help_text=_("This must contains the username of the actor when an action is performed.")
    )
    action = models.CharField(max_length=64, help_text='Action performed.')
    system = models.CharField(
        max_length=64, help_text='Source application that action comes from. E.g: Platform, Olms')
    content_type = models.CharField(max_length=64, null=True, blank=True, help_text='Model Name.')
    object_pk = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    extra = models.TextField(
        null=True, blank=True, help_text='Json Field. Useful to store the serializable target object ')

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return "Author {0} performed action: {1} over {2}-{3} in System {4}".format(
            self.author, self.action, self.content_type, self.object_pk, self.system)

    @classmethod
    def create(cls, author, action, system, **kwargs):
        return cls.objects.create(
            author=author,
            action=action,
            system=system,
            **kwargs
        )
