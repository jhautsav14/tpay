from django.contrib import admin
from .models import *

# Register your models here.
class FluidAdmin(admin.ModelAdmin):
    list_display = ['fluid_name','fluid_price','description']



admin.site.register(Amenities)
admin.site.register(Fluid ,FluidAdmin)
admin.site.register(FluidImages)
admin.site.register(FluidBooking)