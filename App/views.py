from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import psycopg2


# Create your views here.
def home_page_view(request):
    return render(request, 'Home.html')

def receptes_view(request):
    conn = psycopg2.connect(dbname="projecte_final",
                            user="postgres",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas_guia;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'notas_guia': result}
    return render(request, 'Receptes.html', params)

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
                            user="postgres",
                            password="patata")

    dificultat = request.POST["name_dificultat"]
    titol = request.POST["nombre_titulo"]
    nota = request.POST["name_nota"]

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO notas_guia VALUES ('{dificultat}','{titol}','{nota}');")
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('http://127.0.0.1:8000/receptes')


