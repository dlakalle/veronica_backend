# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from veronica_api.models import *

# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Alumno, AlumnoAdmin)
