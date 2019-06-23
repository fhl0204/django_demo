# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Fund(models.Model):
    date = models.DateField(null=True, blank=True, unique=True)
    nav = models.FloatField(null=True, blank=True)
    cav = models.FloatField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.date