from django.shortcuts import render
from catalog.models import Contacts


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефонный номер: {phone_number}\nСообщение: {message}')

        Contacts.objects.create(name=name, phone_number=phone_number, message=message)
    return render(request, 'contacts.html')

