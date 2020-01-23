#Zadanie: Skrypt pokazuje wszystkie dzielniki danej liczby
x=int(input("Wprowadź liczbę: "))
for i in range (1,x):   #Zakres od 1 do danej liczby
    if x%i==0:  #Sprawdzam czy jest dzielnikiem za pomocą modulo
        print(i)    #Jesli tak, drukuje liczbe