def wykres(x,y):
    from pylab import plot, show, xlabel, ylabel, title,legend
    title=input("Podaj nazwę wykresu: ")
    xlabel=input("Nazwij os x: ")
    ylabel=input("Nazwij os y: ")
    legend=([input("Wprowadz nazwę linii x: ")])
    return plot(x,y,"--r")