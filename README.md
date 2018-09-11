# Django History Actions

Django app to track actions/events accross systems.

[![Build Status](https://travis-ci.org/marcosschroh/django-history-actions.svg?branch=master)](https://travis-ci.org/marcosschroh/django-history-actions)
[![codecov](https://codecov.io/gh/marcosschroh/django-history-actions/branch/master/graph/badge.svg)](https://codecov.io/gh/marcosschroh/django-history-actions)
[![GitHub license](https://img.shields.io/github/license/marcosschroh/django-history-actions.svg)](https://github.com/marcosschroh/django-history-actions/blob/master/LICENSE)
![PyPI - Python Version](https://img.shields.io/badge/python-3-blue.svg)


## **Table of Contents**

- [Features](#features)
- [Model Description](#model-description)
- [Quickstart](#quickstart)
- [Sistem Name](#system-name)
- [Signals](#signals)
- [Running Tests](#running-tests)

### Features

1. Save history for your django models.
2. Define global system name or per model
3. Actions apps checker.
4. Signals to track saved models.

### Model Description:

| Field        | Description      | Type | Required | Default             |
|:-------------|:-----------------|:-----|:---------|:--------------------|
| author       | Action author (username)    | str  | True     |                     |
| action       | Action performed | str  | True     |                     |
| system       | System name      | str  | True     | Taken from settings or model instance |
| actor        | Actor involved in the action (username) | str | False    |  |
| created      | Action created Datetime | Datetime |  False   | Auto Generated |
| content_type | Content Type of the model instance | str   | False    | Auto Generated from model instance  |
| object_pk    | Object pk           | int     |  False  | Taken from model instance |
| notes        | Extra note related to the action | TextField     | False        | |
| extra        | Extra field to store serializable objects.          | TextField     |  False       | |

### Quickstart

Install Django History Actions:

```bash
pip install django-history-events
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    ...
    'history_actions',
    ...
)

# Define your System Name
HISTORY_ACTIONS_SYSTEM = 'main'
```

Define your actions.py inside your app

```python
# actions.py

from django.utils.translation import ugettext_lazy as _

INFO_TRAINING_SAVE_ACTION = 'INFO_TRAINING_SAVE_ACTION'

ACTIONS = {
    'INFO_TRAINING_SAVE_ACTION': _('info trainig save action')
}
```

Now you can track History:

```python
from history_actions.manager import HistoryManager

# log an event
HistoryManager.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION')

# log an event linked to a model
model_instance = ModelKlass.objects.first()
HistoryManager.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance=model_instance)

# log an event linked to a model with more info
username = User.ojects.first().username
HistoryActions.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance=model_instance, actor=username, notes='My notes')


# log an event linked to a model and serialize the model
username = User.ojects.first().username
model_instance_dict = model_instance.to_dict()
HistoryActions.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance=model_instance, actor=username, notes='My notes', extra=model_instace_dict)

# use a different system
HistoryActions.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance=model_instance, actor=username, notes='My notes', extra=model_instace_dict, system="custom")
```

If you want to use a diferent system for model tracking, you can define it in:

```python
# models.py

class Chatdentity(MachuBaseModel):
    HISTORY_ACTION_SYSTEM = 'chat'

    user = models.OneToOneField(User)
    user_two = models.OneToOneField(User, related_name='user_manager')
    given_name = models.CharField(
        'Given Name(s)', max_length=200, default='')
    family_name = models.CharField(
        'Family Name(s)', max_length=200, default='')
```

### System Name

The system name is taken from:

1. The `create` method `kwargs`.
2. From `HISTORY_ACTIONS_SYSTEM` variable defined in the `settings.py`.
3. The class variable `HISTORY_ACTION_SYSTEM` defined in the model class.

### Signals

### Running Tests

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```