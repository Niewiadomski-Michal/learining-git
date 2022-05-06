from pkg_resources import add_activation_listener


lista_zakupow = {
    "Piekarnia" : ["Chleb", "Pączek", "Bułki"],
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
}

print (lista_zakupow)
"""
Lista zakupów
Idę do Piekarnia, kupuję tu następujące rzeczy: ['Chleb', 'Pączek', 'Bułki'].
Idę do Warzywniak, kupuję tu następujące rzeczy: ['Marchew', 'Seler', 'Rukola'].
W sumie kupuję 6 produktów.
"""

print ("Lista zakupów:")
print ("Idę do , kupuję następujące rzeczy:")
print (lista_zakupow["Piekarnia"])

print ("Idę do , kupuję następujące rzeczy:")
print (lista_zakupow["Warzywniak"])

liczba_produktow = [6]

for sklep, produkty in lista_zakupow.items():
    print ("Idę do:"), 
    print (sklep.upper()),
    print ("kupuję następujące rzeczy:")
    print (produkty)
print ("W sumie kupuję:") 
print (liczba_produktow)

"""
Zadanie 2
Napisz program, który:

Dla liczb z zakresu od 0 do 100, wyświetli te, które są podzielne przez 5.
W następnym wierszu wyświetli te liczby podniesione do potęgi 3.
"""
podzielne_przez_5 = []
for i in range (1,101):
    if i % 5 == 0:
        podzielne_przez_5.append(i)

szesciany_podzielnych_przez_5 = []

print ("Liczby podzielne przez 5:")
print (podzielne_przez_5)
for i in podzielne_przez_5:
    szesciany_podzielnych_przez_5.append(i*i*i)

print ("Liczby te podniesione do 3 potęgi:")
print (szesciany_podzielnych_przez_5)

print ("teraz już bez pierwszego tekstu, za to z drugim:")
print ("Wspaniale!")
