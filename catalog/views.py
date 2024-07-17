from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView, TemplateView

from catalog.models import Category, Product, Contacts
from .forms import CreateProduct

# Create your views here.


class ContactPageView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            admin_contact = Contacts.objects.get(pk=1).__dict__
            admin_data = {
                "name": admin_contact["name"],
                "address": admin_contact["address"],
                "phone": admin_contact["phone"],
            }
            context["admin_data"] = admin_data
        except Contacts.DoesNotExist:
            return JsonResponse({"error": "Contact not found"}, status=404)
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST["name"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        print({"name": name, "phone": phone, "message": message})
        return self.get(request, *args, **kwargs)


class HomePageView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all().order_by("id")
        paginator = Paginator(products, 3)  # 3 products per page
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj
        return context


class ProdcutDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"


class CreateProductView(CreateView):
    form_class = CreateProduct
    template_name = "catalog/create_product.html"

    def get_success_url(self):
        return "/"
