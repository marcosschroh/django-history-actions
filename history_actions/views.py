# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	HistoryAction,
)


class HistoryActionCreateView(CreateView):

    model = HistoryAction


class HistoryActionDeleteView(DeleteView):

    model = HistoryAction


class HistoryActionDetailView(DetailView):

    model = HistoryAction


class HistoryActionUpdateView(UpdateView):

    model = HistoryAction


class HistoryActionListView(ListView):

    model = HistoryAction

