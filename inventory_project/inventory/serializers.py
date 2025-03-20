from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)

    class Meta:
        model = Inventory
        fields = ["id", "name", "description", "note", "stock", "availability", "supplier_name"]