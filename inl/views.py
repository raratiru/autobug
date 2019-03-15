#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ==============================================================================
#
#       File Name : inl/views.py
#
#       Creation Date : Fri 15 Mar 2019 07:51:16 PM EET (19:51)
#
#       Last Modified : Fri 15 Mar 2019 09:05:56 PM EET (21:05)
#
# ==============================================================================

from dal import autocomplete
from inl import models


class Child2Autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Child2.objects.all()

        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs


class Child3Autocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Child3.objects.all()

        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs


class MasterAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Master.objects.all()

        if self.q:
            qs = qs.filter(id__icontains=self.q)

        return qs
