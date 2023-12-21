from django.urls import path
from datatables import views

urlpatterns = [

    path("datatables/", views.datatables_page, name='datatables'),
    path("data/", views.datatable_json, name='data'),
    path("add_to_cart", views.add_to_cart, name='add_to_cart'),
]
