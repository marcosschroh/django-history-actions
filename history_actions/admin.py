from django.contrib import admin

from history_actions.models import HistoryActions


@admin.register(HistoryActions)
class HistoryActionsAdmin(admin.ModelAdmin):
    list_display = ('author', 'action', 'system', 'created', 'content_type', 'object_pk')

    search_fields = ['action', 'author', 'system', 'created']
