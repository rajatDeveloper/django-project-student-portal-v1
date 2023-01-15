from dashboard.models import Homework, Notes, Todo
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(Notes)
admin.site.register(Homework)
admin.site.register(Todo)