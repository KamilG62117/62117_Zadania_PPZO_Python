
a = 0.0
b = 0.0
wybor = 0

while True:
    print("Podaj liczbe a: ", end="")
    a = float(input())
    print("")
    print("Podaj liczbe b: ", end="")
    b = float(input())
    print("")
    
    while True:
        print("Co chcesz zrobić?")
        print("[0]Zamknij [1]Dodawanie [2]Odejmowanie [3]Mnożenie [4]Dzielenie")
        print("Wybór: ", end="")
        wybor = int(input())
        
        if wybor != 0 and wybor != 1 and wybor != 2 and wybor != 3 and wybor != 4:
            print("Błędny wybór! Spróbuj jeszcze raz.")
        else:
            break
    
    if wybor != 0:
        if wybor == 1:
            print("Wynik dodawania: " + str(a + b))
        elif wybor == 2:
            print("Wynik odejmowania: " + str(a - b))
        elif wybor == 3:
            print("Wynik mnożenia: " + str(a * b))
        elif wybor == 4:
            if b != 0:
                print("Wynik dzielenia: " + str(a / b))
            else:
                print("Nie można dzielić przez zero!")
        
        print("")
        print("Naciśnij Enter, aby wykonać następne obliczenia...")
        input()
        import os
        os.system('clear')
    else:
        break

print("Zamykanie programu...")
