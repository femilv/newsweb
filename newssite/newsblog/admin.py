from django.contrib import admin
from newsblog.models import Category, News

# Register your models here.

admin.site.register(Category)
admin.site.register(News)