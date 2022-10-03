from msilib.schema import AdminUISequence
from django.contrib import admin
from Bus.models import BusList,User

# Register your models here.

admin.site.register(BusList)
admin.site.register(User)
