# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Album, Song, Question, Choice
# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Question)
admin.site.register(Choice)
