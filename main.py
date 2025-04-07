ilosc = 0
suma = 0

print("Podaj ilosc ocen: ", end="")
ilosc = int(str(input()))

if ilosc == 0:
    print("Brak ocen do obliczenia średniej")
else:
    tab = [0] * ilosc
    print("")
    print("Podaj oceny:")

    for i in range(ilosc):
        while True:
            print(f"{i+1}. ", end="")
            tab[i] = int(str(input()))
            if tab[i] >= 1 and tab[i] <= 6:
                suma += tab[i]
                break
            else:
                print("")
                print("Podano złą ocenę, spróbuj ponownie podać ocenę z zakresu 1-6")

    srednia = suma / ilosc
    print("")
    print("Średnia ocen: " + str(srednia))
    print("")

    if srednia >= 3.0:
        print("Uczeń zdał.")
    else:
        print("Uczeń nie zdał.")