from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('v1',
         views.InventoryListView.as_view(),
         name='inventory_list'),
    path('v1/inventory-create',
         views.InventoryCreateView.as_view(),
         name='inventory_create'),
    path('v1/inventory-check',
         views.InventoryCheckView.as_view(),
         name='inventory_check'),
    path('v1/<inventory_name>',
         views.InventoryDetailView.as_view(),
         name='inventory_detail'),
    path('v1/<inventory_name>/delete',
         views.InventoryDeleteView.as_view(),
         name='inventory_delete'),
    path('v1/<inventory_name>/data.json',
         views.InventoryDetailJSONView.as_view(),
         name='inventory_json_detail'),
    path('v1/<inventory_name>/resource-create',
         views.ResourceCreateView.as_view(),
         name='resource_create'),
    path('v1/<inventory_name>/<resource_name>',
         views.ResourceDetailView.as_view(),
         name='resource_detail'),
    path('v1/<inventory_name>/<resource_name>/data.json',
         views.ResourceDetailJSONView.as_view(),
         name='resource_json_detail'),
]
