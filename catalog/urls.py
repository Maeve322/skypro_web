from django.urls import include, path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductDetailView,
    ProductCreateView,
    HomePageView,
    ContactPageView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", HomePageView.as_view(), name="product_list"),
    path(
        "products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path(
        "products/create/", ProductCreateView.as_view(), name="create_product"
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "products/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="delete_product",
    ),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
]
