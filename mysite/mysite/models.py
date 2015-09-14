from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText


class CustomPage(Page, RichText):
    banner = models.ImageField(upload_to="banners")
