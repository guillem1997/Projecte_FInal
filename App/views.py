from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def home_page_view(request):
    return render(request, 'Home.html')

def receptes_view(request):
    return render(request, 'Receptes.html')

def ingredients_view(request):
    return render(request, 'Ingredients.html')
