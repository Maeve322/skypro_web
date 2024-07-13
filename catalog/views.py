from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator

from catalog.models import Category, Product, ContactsView
from .forms import CreateProduct

# Create your views here.


def get_contact_page(request):
    try:
        admin_contact = ContactsView.objects.get(pk=1).__dict__
        admin_data = {
            "name": admin_contact["name"],
            "address": admin_contact["address"],
            "phone": admin_contact["phone"],
        }

        if request.method == "POST":
            name = request.POST["name"]
            phone = request.POST["phone"]
            message = request.POST["message"]
            print({"name": name, "phone": phone, "message": message})

        return render(
            request, "catalog/contacts.html", {"admin_data": admin_data}
        )
    except ContactsView.DoesNotExist:
        return JsonResponse({"error": "Contact not found"}, status=404)


def get_home_page(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)  # 3 products per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "catalog/home.html", {"page_obj": page_obj})


def product_details(request, pk):
    product_detail = Product.objects.get(pk=pk)
    return render(
        request, "catalog/product_detail.html", {"product": product_detail}
    )


def create_product(request):
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateProduct()
    return render(request, "catalog/create_product.html", {"form": form})
