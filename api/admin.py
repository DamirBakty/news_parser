from django.contrib import admin
from .models import Resource, Item
# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


admin.site.register(Resource)
admin.site.register(Item, ItemsAdmin)
