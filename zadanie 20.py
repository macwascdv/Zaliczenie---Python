#Zadanie 20
def tlumacz(slowo):
    slownik = {"styczen":"january","luty":"february","marzec":"march",
               "kwiecien":"april","maj":"may","czerwiec":"june","lipiec":"july",
               "sierpien":"august","wrzesien":"september","pazdziernik":"october",
               "listopad":"november","grudzien":"december"}
    wynik=slownik[slowo]
    return wynik