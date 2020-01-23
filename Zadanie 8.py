#zadanie 8: Sprawdzian i oceny
makspunktow=50
punkty=int(input("Wpisz uzyskany wynik punktowy: "))
proc=(punkty/makspunktow)*100
if proc<=39:
    print("NDST")
elif proc>=40 and proc<=49:
    print("DOP")
elif proc>=50 and proc<=69:
    print("DST")
elif proc>=70 and proc<=84:
    print("DB")
elif proc>=84 and proc<=99:
    print("BDB")
else:
    print("CEL")