# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Member
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'request_status')
    list_filter = ('sex', 'request_status')
    search_fields = ('first_name', 'request_status')

admin.site.register(Member, MemberAdmin)
