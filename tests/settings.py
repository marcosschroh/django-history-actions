# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k31_)zzq8)fy+$#_s_yl*cw$-53uiak#ph0q)_@k+cgi)v0#+_"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "tests.app_test",
    "history_actions",
]

SITE_ID = 1

MIDDLEWARE_CLASSES = ()

HISTORY_ACTIONS_SYSTEM = "main"
