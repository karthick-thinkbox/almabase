from django.contrib import admin
from .models import Inventory


class inv_admin(admin.ModelAdmin):
    search_fields=('title',)
#admin.site.register(inventory)
admin.site.register(Inventory,inv_admin)

# Register your models here.
