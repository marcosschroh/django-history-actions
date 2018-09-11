# Django History Actions

Django app to track all events accross the system.

## Documentation

-----------------

## Quickstart

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
HISTORY_ACTIONS_SYSTEM = 'platform'
```

### Model Fields:

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

HistoryManager.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION')

model_instance = ModelKlass.objects.first()
HistoryManager.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance)

username = User.ojects.first().username
HistoryActions.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance, actor=username, notes='My notes')


username = User.ojects.first().username
model_instance_dict = model_instance.to_dict()
HistoryActions.create(
    'an_author', 'INFO_TRAINING_SAVE_ACTION', model_instance, actor=username, notes='My notes', extra=model_instace_dict)
```

If you want to use a diferent system for model tracking, you can define it in:

```python
# models.py

class LQIdentity(MachuBaseModel):
    HISTORY_ACTION_SYSTEM = 'olms'

    user = models.OneToOneField(User)
    user_two = models.OneToOneField(User, related_name='user_manager')
    given_name = models.CharField(
        'Given Name(s)', max_length=200, default='')
    family_name = models.CharField(
        'Family Name(s)', max_length=200, default='')
```

### Features

1. Save history for your django models.
2. Define global system name or per model
3. Actions apps checker.
4. Signal to track saved models.

### Running Tests

Does the code actually work?

```bash
source <YOURVIRTUALENV>/bin/activate
(myenv) $ pip install tox
(myenv) $ tox
```