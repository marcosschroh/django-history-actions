# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'history_actions'
urlpatterns = [
    url(
        regex="^HistoryAction/~create/$",
        view=views.HistoryActionCreateView.as_view(),
        name='HistoryAction_create',
    ),
    url(
        regex="^HistoryAction/(?P<pk>\d+)/~delete/$",
        view=views.HistoryActionDeleteView.as_view(),
        name='HistoryAction_delete',
    ),
    url(
        regex="^HistoryAction/(?P<pk>\d+)/$",
        view=views.HistoryActionDetailView.as_view(),
        name='HistoryAction_detail',
    ),
    url(
        regex="^HistoryAction/(?P<pk>\d+)/~update/$",
        view=views.HistoryActionUpdateView.as_view(),
        name='HistoryAction_update',
    ),
    url(
        regex="^HistoryAction/$",
        view=views.HistoryActionListView.as_view(),
        name='HistoryAction_list',
    ),
	]
