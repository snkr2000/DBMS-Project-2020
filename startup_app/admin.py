from django.contrib import admin
from .models import StartUps, Investors, Investment_table, Jobs, Job_Seekers
# Register your models here.

admin.site.register(StartUps)
admin.site.register(Investors)
admin.site.register(Investment_table)
admin.site.register(Jobs)
admin.site.register(Job_Seekers)
