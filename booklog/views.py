# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse

# Create your views here.


def index_view(request):
    return HttpResponse("It works!")