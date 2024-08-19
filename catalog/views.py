from django.shortcuts import render, get_object_or_404
from catalog.models import Contacts, Product
from django.core.paginator import Paginator


def products(request, page_number=1):
    products_set = Product.objects.all()

    per_page = 6
    paginator = Paginator(products_set, per_page)
    products_paginator = paginator.page(page_number)

    context = {"products": products_paginator}
    return render(request, 'products.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_details.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        print(f'Имя: {name}, Телефонный номер: {phone_number}\nСообщение: {message}')

        Contacts.objects.create(name=name, phone_number=phone_number, message=message)
    return render(request, 'contacts.html')


def new_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_picture = request.POST.get('product_picture')
        category = request.POST.get('category')
        price = request.POST.get('price')

        Product.objects.create(product_name=product_name,
                               product_description=product_description,
                               product_picture=product_picture,
                               category=category,
                               price=price)
    return render(request, 'new_product.html')
