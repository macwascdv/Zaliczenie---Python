#Zadanie 33
#Sprawdzenie ilosci zywych komore - m to macierz
import numpy as np
def mk(n):
    return np.random.choice([255,0], size=n**2, p=[0.4,0.6]).reshape(n,n)
def addGlider(i, j, grid):
    glider = np.array([[0, 0, 255], [255, 0, 255], [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider
    return grid
def addBochenek(i,j,grid):
    loaf = np.array([[0,255,255,0],[255,0,0,255],[0,255,0,255],
                      [0,0,255,0]])
    grid[i:i+4, j:j+4] = loaf
    return grid
def addCegla(i,j,grid):
    block = np.array([[255,255],[255,255]])
    grid[i:i+2, j:j+2] = block
    return grid
def addBeehive(i,j,grid):
    beehive = np.array([[0,255,255,0],[255,0,0,255],[0,255,255,0]])
    grid [i:i+3,j:j+4] = beehive
    return grid
def addBoat(i,j,grid):
    boat = np.array([[255,255,0],[255,0,255],[0,255,0]])
    grid [i:i+3,j:j+3] = boat
    return grid
def addBlinker(i,j,grid):
    blinker = np.array([[255],[255],[255]])
    grid [i:i+3,j:j] = blinker
    return grid
def addToad(i,j,grid):
    toad = np.array([[0,255,255,255],[255,255,255,0]])
    grid [i:i+2,j:j+4] = toad
    return grid
def addBeacon(i,j,grid):
    beacon = np.array([[255,255,0,0],[255,0,0,0],[0,0,0,255],[0,0,255,255]])
    grid [i:i+4,j:j+4] = beacon
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