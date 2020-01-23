#Zadanie 10
#Pierwsza metoda - wlasne funkcje
def srednia(a):
        suma=0
        for i in a:
            suma=suma+i
        srednia=suma/len(a)
        return(srednia)

def odchylenie(a):
    gora=0
    for i in a:
        gora=gora+(i-srednia(a))**2
    dol=len(a)
    wynik=(gora/dol)**0.5
    return(wynik)

x=int(input("Podaj liczbe elementow"))
lista=[]
for i in range(x):
    lista.append(int(input("Podaj liczbe: ")))
print (f"Twoja srednia wynosi {srednia(lista)}")
print (f"Twoje odchylenie wynosi {odchylenie(lista)}")

#Teraz gotowymi metodami
from numpy import mean, std
srednia2= mean(lista)
odchylenie2=std(lista)
print (f"Twoja srednia wynosi {srednia2}")
print (f"Twoje odchylenie wynosi {odchylenie2}")