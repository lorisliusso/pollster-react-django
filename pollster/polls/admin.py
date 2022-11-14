from django.contrib import admin
from .models import Question, Choice

admin.site.site_header= 'Pollster Admin'
admin.site.site_title= 'Pollster Admin Area'
admin.site.index_title= 'Welcome to the Pollster admin area'


admin.site.register(Question)
admin.site.register(Choice)