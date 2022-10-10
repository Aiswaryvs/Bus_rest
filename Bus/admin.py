from msilib.schema import AdminUISequence
from django.contrib import admin
from Bus.models import*

# Register your models here.

admin.site.register(BusList)
admin.site.register(User)
# admin.site.register(Price)
admin.site.register(Reservation)
