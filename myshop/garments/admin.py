from django.contrib import admin
from garments.models import FormalShirts

class FormalShirtsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created', 'update')
     

# Register your models here.
admin.site.register(FormalShirts, FormalShirtsAdmin)