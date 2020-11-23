from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
import psycopg2


# Create your views here.
def home_page_view(request):
    return render(request, 'Home.html')


def receptes_view(request):
    conn = psycopg2.connect(dbname="Projecte_Final",
                            user="postgres",
                            password="patata")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM plats;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    params = {'plats': result}
    return render(request, 'Receptes.html', params)


def ingredients_view(request):
    return render(request, 'Ingredients.html')


def insert(request):
    conn = psycopg2.connect(dbname="Projecte_Final",
                            user="postgres",
                            password='patata')

    kcal            =   request.POST["name_Kcal"]
    carbohidrates   =   request.POST["name_Carbohidrates"]
    proteina        =   request.POST["name_Proteina"]
    grasas          =   request.POST["name_Grasas"]
    fibra           =   request.POST["name_Fibra"]
    omnivore        =   request.POST["value_Omnivore"]
    vegetarian      =   request.POST["value_Vegetarian"]
    vegan           =   request.POST["value_Vegan"]
    milk            =   request.POST["value_Milk"]
    eggs            =   request.POST["value_Eggs"]
    fish            =   request.POST["value_Fish"]
    crustaceans     =   request.POST["value_Crustaceans"]
    nuts            =   request.POST["value_Nuts"]
    peanut          =   request.POST["value_Peanuts"]
    gluten          =   request.POST["value_Gluten"]
    soy             =   request.POST["value_Soy"]
    january         =   request.POST["value_January"]
    february        =   request.POST["value_February"]
    mars            =   request.POST["value_Mars"]
    april           =   request.POST["value_April"]
    may             =   request.POST["value_May"]
    jun             =   request.POST["value_Jun"]
    july            =   request.POST["value_July"]
    august          =   request.POST["value_August"]
    september       =   request.POST["value_September"]
    october         =   request.POST["value_October"]
    november        =   request.POST["value_November"]
    december        =   request.POST["value_December"]

    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO ingredients VALUES ('{kcal}', '{carbohidrates}','{proteina}','{grasas}','{fibra}',"
                   f"'{omnivore}','{vegetarian}','{vegan}','{milk}','{eggs}','{fish}','{crustaceans}',"
                   f"'{nuts}',{peanut}',{gluten}',{soy}',{january}',{february}',{mars}',{april}',{may}',{jun}',"
                   f"{july}',{august}',{september}',{october}',{november}',{december}');")
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


