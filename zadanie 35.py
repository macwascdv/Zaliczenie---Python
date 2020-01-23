#zadadnie 35
class Kwadrat():
    def __init__(self, bok):
        self.bok=bok
        
    def krawedz(self):
        return self.bok
    def wyswietl(self):
        return print(self)
    def pole(self):
        a=self.bok
        wynik=a**2
        return wynik
    def obwod(self):
        a=self.bok
        wynik=a*4
        return wynik