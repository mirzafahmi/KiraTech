from django.shortcuts import render
from django.conf import settings
import requests
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from django.db.models import Q

from .models import Inventory
from .serializers import InventorySerializer

class InventoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Inventory.objects.select_related("supplier").all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get("name")
        supplier_name = self.request.query_params.get("supplier_name")

        if name:
            queryset = queryset.filter(Q(name__icontains=name))

        if supplier_name:
            queryset = queryset.filter(supplier__name__icontains=supplier_name)

        return queryset
    
class InventoryListView(ListView):
    template_name = "inventory_list.html"
    context_object_name = "inventories"

    def get_queryset(self):
        api_url = "http://localhost:8000/api/inventory/"

        if hasattr(settings, "TEST_SERVER_URL"):
            api_url = settings.TEST_SERVER_URL + "/api/inventory/"

        response = requests.get(api_url)
        return response.json() if response.status_code == 200 else []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventories"] = self.get_queryset() 
        return context

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = "inventory_detail.html"
    context_object_name = "inventory"

    def get_object(self):
        return get_object_or_404(Inventory, pk=self.kwargs["pk"])
