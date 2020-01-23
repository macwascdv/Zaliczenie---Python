def funk_lin(a,b):
    from pylab import plot
    dol=int(input("Podaj dolny zakres x: "))
    gora=int(input("Podaj górny zakres x: "))
    x=list(range(dol,gora))
    y=[a*i+b for i in x]
    print(f"\n\tLista x: {x}, \n\tlista y: {y}")
    return plot(x,y)

def funk_kwad(a,b,c):
    from pylab import plot
    dol=int(input("Podaj dolny zakres x: "))
    gora=int(input("Podaj górny zakres x: "))
    x=list(range(dol,gora))
    y=[(a*(i**2)+(b*i)+c) for i in x]
    print(f"\n\tLista x: {x}, \n\tlista y: {y}")
    return plot(x,y)


def funk_odwr(a):
    from pylab import plot
    dol=int(input("Podaj dolny zakres x: "))
    gora=int(input("Podaj górny zakres x: "))
    x=list(range(dol,gora))
    y=[a/i**len(x) if i!=0 else None for i in x]
    print(f"\n\tLista x: {x}, \n\tlista y: {y}")
    return plot(x,y)

def f_odwrotnie(a,n):
    from pylab import plot
    x = [i for i in range(-100,100)]
    y = [a/x**n if x!=0  else None for x in x]
    return plot(x,y)