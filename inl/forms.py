#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : inl/forms.py
#
#       Creation Date : Fri 15 Mar 2019 08:36:07 PM EET (20:36)
#
#       Last Modified : Fri 15 Mar 2019 09:23:27 PM EET (21:23)
#
# ==============================================================================

from dal import autocomplete
from django import forms
from inl import models


class Child1Form(forms.ModelForm):
    class Meta:
        model = models.Child1
        fields = ('__all__')
        widgets = {
            'key': autocomplete.ModelSelect2(url='master'),
        }


class Child2Form(forms.ModelForm):
    class Meta:
        model = models.Child2
        fields = ('__all__')
        widgets = {
            'child_key': autocomplete.ModelSelect2(url='child2'),
            'key': autocomplete.ModelSelect2(url='master'),
        }


class Child3Form(forms.ModelForm):
    class Meta:
        model = models.Child3
        fields = ('__all__')
        widgets = {
            'child_keys': autocomplete.ModelSelect2Multiple(url='child3'),
            'key': autocomplete.ModelSelect2(url='master'),
        }
