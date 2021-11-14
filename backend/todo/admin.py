from django.contrib import admin

import todo

from .models import ToDo
admin.site.register(ToDo)
