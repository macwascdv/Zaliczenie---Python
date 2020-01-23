#zadanie 15
#Pierwsza lista
from pylab import plot, show, xlabel, ylabel, title, legend, savefig
Poznan=[6,5,6,6,9,9,7,7,5,4,5,5,5,3]
#Druga lista
Tunis=[15,16,13,17,14,15,15,14,17,15,14,13,16,14]
#Trzecia lista
Tokio=[11,9,12,12,10,10,6,8,8,8,10,11,10,11]
#Ilosc dni
dni=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#Mamy dane, tworzymy wykres
plot(dni,Poznan,"-*")
plot(dni,Tunis,"-or")
plot(dni,Tokio,"-db")
title("Temperatura na najlblizsze 14 dni")
xlabel("dzień")
ylabel("Temperatura (Celsjusz)")
legend(["Poznan","Tunis","Tokio"])