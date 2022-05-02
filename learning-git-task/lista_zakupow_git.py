lista_zakupow = {
    "Piekarnia" : ["Chleb", "Pączek", "Bułki"],
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
    }

print (lista_zakupow)

for sklep, produkty in lista_zakupow.items():
    print ("Idę do:"), 
    print (sklep),
    print ("kupuję następujące rzeczy:")
    print (produkty)
