from django.shortcuts import render
from django.shortcuts import HttpResponse
import psycopg2


# Create your views here.
def home_page_view(request):
    return render(request, 'Home.html')

def receptes_view(request):
    return render(request, 'Receptes.html')

def ingredients_view(request):
    return render(request, 'Ingredients.html')

def insert(request):
    conn = psycopg2.connect(dbname="projecte_final",
                            user="aram",
                            password='patata')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ingredients VALUES ('moniato', 'tardor');")
    conn.commit()
    cursor.close()
    conn.close()

    return HttpResponse('Insertado')

def select(request):
    conn = psycopg2.connect(dbname="projecte_final",
                            user="aram",
                            password='patata')
    cursor = conn.cursor()
    cursor.execute("select * from ingredients")
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return HttpResponse(result)

def anadir(request):
    conn = psycopg2.connect(dbname="projecte_final",
                            user="aram",
                            password="patata")
    return HttpResponse('insertado')

