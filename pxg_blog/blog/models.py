#from .utils import slugify
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.sitemaps import Sitemap
from django.db import models
from django.db.models import permalink
#from minicms.models import BaseContent
from random import choice
from string import ascii_letters, digits
import re


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)

    # System fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
