# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from forms import AddForm


def index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForm()
    return render(request, 'my_app/home.html', {'form': form})


def add(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return HttpResponse(str(a + b))
