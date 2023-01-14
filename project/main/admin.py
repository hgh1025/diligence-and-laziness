from django.contrib import admin

# Register your models here.
from . models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Working_condition)
admin.site.register(Commute)
admin.site.register(Pay)
admin.site.register(Vacation)