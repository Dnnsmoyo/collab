# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Feed, Profile
# Register your models here.
admin.site.register(Feed)
admin.site.register(Profile)