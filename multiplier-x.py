antwoord = input("Van welk nummer wilt u de tafel hebben? ")

def tafelVan(nummer):
    for x in range(1, 11):
        print(str(x) + " * " + nummer + " = " + str(x * int(nummer)))

tafelVan(antwoord)