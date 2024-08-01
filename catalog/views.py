from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефонный номер: {phone_number}\nСообщение: {message}')
    return render(request, 'contacts.html')

