from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import CustomPage

custom_page_extra_fieldsets = ((None, {"fields": ("banner",)}),)


class CustomPageAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + custom_page_extra_fieldsets

admin.site.register(CustomPage, PageAdmin)
