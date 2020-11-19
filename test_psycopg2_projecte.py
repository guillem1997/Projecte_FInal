import psycopg2
conn = psycopg2.connect(dbname="projecte_final", user="aram", password="patata")
print("Funciona!")