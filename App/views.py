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


def new_ingredient(request):
    new_post = {}
    for clau in request.POST:
        if request.POST[clau] == "":
            new_post[clau] = None
        else:
            new_post[clau] = request.POST[clau]
    request.POST = new_post
    conn = psycopg2.connect(dbname="Projecte_Final",
                            user="postgres",
                            password="patata")

    name = request.POST["value_ingredient"]
    kcal = request.POST["value_Kcal"]
    carbohidrates = request.POST["value_Carbohidrates"]
    proteina = request.POST["value_Proteina"]
    grasas = request.POST["value_Grasas"]
    fibra = request.POST["value_Fibra"]
    omnivore = request.POST["value_Omnivore"]
    vegetarian = request.POST["value_Vegetarian"]
    vegan = request.POST["value_Vegan"]
    milk = request.POST["value_Milk"]
    eggs = request.POST["value_Eggs"]
    fish = request.POST["value_Fish"]
    crustaceans = request.POST["value_Crustaceans"]
    nuts = request.POST["value_Nuts"]
    peanut = request.POST["value_Peanuts"]
    gluten = request.POST["value_Gluten"]
    soy = request.POST["value_Soy"]
    january = request.POST["value_January"]
    february = request.POST["value_February"]
    mars = request.POST["value_Mars"]
    april = request.POST["value_April"]
    may = request.POST["value_May"]
    jun = request.POST["value_Jun"]
    july = request.POST["value_July"]
    august = request.POST["value_August"]
    september = request.POST["value_September"]
    october = request.POST["value_October"]
    november = request.POST["value_November"]
    december = request.POST["value_December"]

    cursor = conn.cursor()

    cursor.execute("INSERT INTO ingredients VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
                   "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, kcal, carbohidrates, proteina,
                                                                                   grasas, fibra, omnivore, vegetarian,
                                                                                   vegan, milk, eggs, fish, crustaceans,
                                                                                   nuts, peanut, gluten, soy, january,
                                                                                   february, mars, april, may, jun,
                                                                                   july,
                                                                                   august, september, october, november,
                                                                                   december))

    print(f"INSERT INTO ingredients VALUES ('{name}','{kcal}','{carbohidrates}','{proteina}','{grasas}',"
          f"'{fibra}','{omnivore}','{vegetarian}','{vegan}','{milk}','{eggs}','{fish}','{crustaceans}',"
          f"'{nuts}','{peanut}','{gluten}','{soy}','{january}','{february}','{mars}','{april}','{may}',"
          f"'{jun}','{july}','{august}','{september}','{october}','{november}','{december}');")
    conn.commit()
    cursor.close()
    conn.close()

    return redirect("http://127.0.0.1:8000/ingredients")


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

def recipes_view(request):
    return render(request, 'inserts_receptes.html')

def new_recipe(request):
    conn = psycopg2.connect(dbname="Projecte_Final",
                            user="postgres",
                            password="patata")

    title = request.POST["value_title"]
    time = request.POST["value_time"]
    difficulty = request.POST["value_difficulty"]
    description = request.POST["value_description"]

    cursor = conn.cursor()

    cursor.execute("INSERT INTO plats VALUES (default, %s, %s, %s, %s)", (title, time, difficulty, description))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect("http://127.0.0.1:8000/recipes")
