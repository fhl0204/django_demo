# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from forms import AddForm
from .models import Fund
from django.http import Http404


def fund(requset):
    #funds = get_object_or_404(Fund)
    funds = Fund.objects.all()
    return render(requset, 'my_app/fund.html', {'funds': funds})
