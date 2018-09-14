from django.contrib import admin

from tests.app_test import models


admin.site.register(models.Profile)
admin.site.register(models.SuperProfile)
admin.site.register(models.ProfilePostSaveSignal)
