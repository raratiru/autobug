#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : inl/models.py
#
#       Creation Date : Fri 15 Mar 2019 07:51:16 PM EET (19:51)
#
#       Last Modified : Fri 15 Mar 2019 09:20:49 PM EET (21:20)
#
# ==============================================================================

from django.db import models


class Master(models.Model):
    pass


class Child1(models.Model):
    key = models.ForeignKey(Master, on_delete=models.PROTECT)
    boolean = models.BooleanField()


class Child2(models.Model):
    key = models.ForeignKey(Master, on_delete=models.PROTECT)
    boolean = models.BooleanField()
    child_key = models.ForeignKey(Child1, on_delete=models.PROTECT)


class Child3(models.Model):
    key = models.ForeignKey(Master, on_delete=models.PROTECT)
    child_keys = models.ManyToManyField(Child2)
    boolean = models.BooleanField()
