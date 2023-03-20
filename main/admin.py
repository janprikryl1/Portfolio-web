from django.contrib import admin
from .models import Message, Screenshot, Project

# Register your models here.

admin.site.site_header = 'Správce osobní stránky'

admin.site.register(Message)
admin.site.register(Screenshot)
admin.site.register(Project)