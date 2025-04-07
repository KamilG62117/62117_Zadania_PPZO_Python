
wybor = 0
stopnie = 0.0

while True:
    print("Wybierz rodzaj konwersji:")
    print("[0]Zamknij [1]Ze stopni Celsjusza na Fahrenheita [2]Ze stopni Fahrenheita na Celsjusza")
    print("Wybór: ", end="")
    wybor = int(input())

    while True:
        if wybor != 0 and wybor != 1 and wybor != 2:
            print("Błędny wybór! Spróbuj jeszcze raz.")
            print("Wybór: ", end="")
            wybor = int(input())
        else:
            break

    if wybor != 0:
        if wybor == 1:
            print("Podaj stopnie Celsjusza: ", end="")
            stopnie = float(input())
            print("Stopnie Fahrenheita: " + str(stopnie * 1.8 + 32))
        elif wybor == 2:
            print("Podaj stopnie Fahrenheita: ", end="")
            stopnie = float(input())
            print("Stopnie Celsjusza: " + str((stopnie - 32) / 1.8))

        print("")
        print("Naciśnij Enter, aby wykonać następną konwersje...")
        input()
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        break

print("Zamykanie programu...")