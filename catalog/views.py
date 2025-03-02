from django.shortcuts import render


def index(request):
    return render(request, 'catalog/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        with open('catalog/text.txt', 'w', encoding="utf-8") as f:
           f.write(f'{name}\n{phone}\n{message}\n')

    return render(request, 'catalog/contacts.html')