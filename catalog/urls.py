from django.urls import include, path
from .views import (
    get_contact_page,
    get_home_page,
    product_details,
    create_product,
)

urlpatterns = [
    path("", get_home_page, name="product_list"),
    path("products/<int:pk>/", product_details, name="product_detail"),
    path("products/create/", create_product, name="create_product"),
    path("contacts/", get_contact_page, name="contacts"),
]
