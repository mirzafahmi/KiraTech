from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, InventoryListView, InventoryDetailView

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename="inventory/")

urlpatterns = [
    path("inventory/", InventoryListView.as_view(), name="inventory-list"),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path("api/", include(router.urls)),
]
