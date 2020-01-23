#zadanie 28 #funkcja bez gotowych funkcji
def srednia(x):
    suma=0
    for i in x:
        suma=suma+i
    return (suma)
def korelacja(x,y):
    #Teraz wyliczam licznik:
    suma1=0
    for i in range (len(x)): #pierwszy element licznika
        suma1=suma1+(x[i]*y[i])
    suma2=sum(x)*sum(y) #drugi el. licznika
    gora=(len(x)*suma1)-suma2 #licze caly licznik
    #teraz mianownik
    sumakwadratowx=0
    kwadratsumyx=0
    sumakwadratowy=0
    kwadratsumyy=0
    for i in range (len(x)):
        sumakwadratowx=sumakwadratowx+x[i]**2
        kwadratsumyx=sum(x)**2
        sumakwadratowy=sumakwadratowy+y[i]**2
        kwadratsumyy=sum(y)**2
    czesc_x=(len(x)*sumakwadratowx)-kwadratsumyx
    czesc_y=(len(x)*sumakwadratowy)-kwadratsumyy
    dol=(czesc_x*czesc_y)**0.5
    wynik=gora/dol
    return (wynik)

#Wersja z biblioteka
from scipy.stats import pearsonr
x=[12,20,-10]
y=[-5,-6,12]
kor=pearsonr(x,y)
print(f"Korelacja wynosi: {kor[0]}")