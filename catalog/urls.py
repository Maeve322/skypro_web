from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductDetailView,
    ProductCreateView,
    HomePageView,
    ContactPageView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryListView,
)

app_name = CatalogConfig.name


# urlpatterns = [

#     path('product/<int:pk>/', cache_page(60 * 15)(views.ProductDetailView.as_view()), name='specific_product'),  # просмотр продукта
#
# ]

urlpatterns = [
    path("", HomePageView.as_view(), name="product_list"),
    path(
        "products/<int:pk>/",
        cache_page(60 * 15)(ProductDetailView.as_view()),
        name="product_detail",
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
    path("category", CategoryListView.as_view(), name="category_list"),
]
