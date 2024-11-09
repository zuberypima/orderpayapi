from django.urls import path
from .views import ProductListView,OrderDetailsListView

urlpatterns = [
    path('api/products/', ProductListView.as_view(), name='products'),  # Added trailing slash
    path('api/oderdetails/', OrderDetailsListView.as_view(), name='oderdetails'),  # Added trailing slash

]
