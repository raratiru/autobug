#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : inl/admin.py
#
#       Creation Date : Fri 15 Mar 2019 07:51:16 PM EET (19:51)
#
#       Last Modified : Thu 21 Mar 2019 05:18:58 PM EET (17:18)
#
# ==============================================================================

from django.contrib import admin
from inl import models
from inl import forms


class Child1Inline(admin.StackedInline):
    model = models.Child1
    min_num = 1
    extra = 0


class Child2Inline(admin.StackedInline):
    model = models.Child2
    min_num = 1
    extra = 0
    autocomplete_fields = ('child_key', )
    # form = forms.Child2Form   # Uncomment to enable django-autocomplete-light


class Child3Inline(admin.StackedInline):
    model = models.Child3
    min_num = 1
    extra = 0
    autocomplete_fields = ('child_keys', )
    # form = forms.Child3Form  # Uncomment to enable django-autocomplete-light

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('child_keys')


@admin.register(models.Master)
class MasterAdmin(admin.ModelAdmin):
    search_fields = ('id', )
    inlines = (Child1Inline, Child2Inline, Child3Inline, )


@admin.register(models.Child1)
class Child1Admin(admin.ModelAdmin):
    search_fields = ('id', )
    autocomplete_fields = ('key', )
    # form = forms.Child1Form  # Uncomment to enable django-autocomplete-light


@admin.register(models.Child2)
class Child2Admin(admin.ModelAdmin):
    search_fields = ('id', )
    autocomplete_fields = ('key', 'child_key')
    # form = forms.Child2Form  # Uncomment to enable django-autocomplete-light


@admin.register(models.Child3)
class Child3Admin(admin.ModelAdmin):
    search_fields = ('id', )
    autocomplete_fields = ('key', 'child_keys')
    # form = forms.Child3Form  # Uncomment to enable django-autocomplete-light
