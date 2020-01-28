#Zadanie 33
#Sprawdzenie ilosci zywych komore - m to macierz
import numpy as np
def mk(n):
    return np.random.choice([0], size=n**2,).reshape(n,n)

def addBochenek(i,j,grid):
    loaf = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],
                      [0,0,255,0]])
    grid[i:i+4, j:j+4] = loaf
    return grid

def doa(i,j,macierz):
    def komorka(i, j):
        return 0 <= i < len(macierz) and 0 <= j < len(macierz) and macierz[i][j]

    sasiedzi = 0

    if komorka(i-1, j-1) != 0:
        sasiedzi += 1
    if komorka(i-1, j) != 0:
        sasiedzi += 1
    if komorka(i-1, j+1) != 0:
        sasiedzi += 1
    if komorka(i, j-1) != 0:
        sasiedzi += 1
    if komorka(i, j+1) != 0:
        sasiedzi += 1
    if komorka(i+1, j-1) != 0:
        sasiedzi += 1
    if komorka(i+1, j) != 0:
        sasiedzi += 1
    if komorka(i+1, j+1) != 0:
        sasiedzi += 1

    return sasiedzi

macierz=mk(6)

macierz=addBochenek(2,2,macierz)
print (macierz)
print(doa(3,3,macierz))
