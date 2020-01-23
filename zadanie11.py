#zadanie 11
#Obliczyc silnie 2 metodami
#1 metoda - iteracyjnie
r=int(input("Podaj liczbe, ktorej silnie chcesz policzyc: "))
silnia=1
for i in range (1,r+1):
    silnia=silnia*i
print (silnia)
#2 metoda - rekurencyjnie
def silnia(x):
    if x==1:
        return 1
    else:
        return x*silnia(x-1)