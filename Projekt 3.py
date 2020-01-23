import numpy as np
import math
class Vector2D():
    def __init__(self, x,y):
        self.x = x
        self.y = y
#utworz funkcje
#1. wyswietlanie wspolrzednych
#2. Dodawanie kolejnego wektora (suma)
#3. Odejmowanie drugiego
#4. iloczyn przez liczbe
#5. iloczyn przez drugi wektor skalarny
#6. Obroc o dany kat
#7. Modul
#8. Wyznaczanie wektora przeciwnego
    def wyswietl(self):
        return (self.x,self.y)
    def dodaj(self,b):
        self.x=self.x+b.x
        self.y=self.y+b.y
        print(self.y,self.y)
    def odejmij(self,b):
        self.x=self.x-b.x
        self.y=self.y-b.y
        print(self.x,self.y)
    def pomnozliczbe(self,l):
        self.x=self.x*l
        self.y=self.y*l
        print(self.x,self.y)
    def iloczynskalarny(self,b):
        self.x=self.x*b.x
        self.y=self.y*b.y
        print(self.x,self.y)
    def modul(self):
        m=(self.x**2+self.y**2)**0.5
        print(m)
    def przeciwny(self):
        self.x= -self.x
        self.y= -self.y
        print(self.x,self.y)
    def obroc(self,k):
        kat_alfa=k*math.pi/180
        sin=math.sin(kat_alfa)
        cos=math.cos(kat_alfa)
        x=self.x
        y=self.y
        self.x=x*cos-y*sin
        self.y=x*sin+y*cos
        print(self.x,self.y)