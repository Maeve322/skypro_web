from django.shortcuts import render
from django.http import JsonResponse

from catalog.models import Category, Product,ContactsView
# Create your views here.

def get_contact_page(request):
    admin_contact = ContactsView.objects.get(pk=1).__dict__
    admin_data = {
        'name': admin_contact['name'],
        'address': admin_contact['address'],
        'phone': admin_contact['phone'],
    }

    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        print({'name': name, 'phone': phone, 'message': message})
    
    return render(request, 'catalog/contacts.html', {'admin_data': admin_data})

def get_home_page(request):
    latest_product = Product.objects.order_by('-created_at')[:5]
    print(latest_product)
    return render(request, 'catalog/home.html')

