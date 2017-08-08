# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
    return render(request, 'statistic/home.html',{})
