from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")

def news(request):
    return render(request, "news.html")

def partners(request):
    return render(request, "partners.html")

def pharmacies(request):
    return render(request, "pharmacies.html")