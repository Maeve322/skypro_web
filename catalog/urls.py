from django.urls import include, path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProdcutDetailView,
    CreateProductView,
    HomePageView,
    ContactPageView,
    ProductUpdateView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="product_list"),
    path(
        "products/<int:pk>/", ProdcutDetailView.as_view(), name="product_detail"
    ),
    path(
        "products/create/", CreateProductView.as_view(), name="create_product"
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="update_product",
    ),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
]
