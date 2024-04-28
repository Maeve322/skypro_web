from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def get_contact_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['phone']
        message = request.POST['message']
        print({'name': name, 'email': email, 'message': message})
    return render(request, 'catalog/contacts.html')

def get_home_page(request):
    return render(request, 'catalog/home.html')

