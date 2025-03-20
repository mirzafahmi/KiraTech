from django.contrib import admin
from .models import Inventory, Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'supplier', 'stock', 'availability']  
    list_filter = ['name']
    search_fields = ['name']  
