from django.contrib import admin

# Register your models here.
from .models import Category, Tag, Blog

admin.site.register([Category, Tag, Blog])