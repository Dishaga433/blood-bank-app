from django.contrib import admin

from main_app import models

# # Register your models here.
# admin.site.register(models.Employee)

admin.site.register(models.Login)
admin.site.register(models.Donor)
admin.site.register(models.Receiver)
admin.site.register(models.Receiver_request)
admin.site.register(models.Feedback)