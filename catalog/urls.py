from django.urls import include,path
from .views import get_contact_page,get_home_page

urlpatterns = [
    path('', get_home_page),
    path('contacts/', get_contact_page),
]
