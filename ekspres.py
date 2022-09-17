# Napisz program do kawy, ktory pilnuje zasobów i wyświetla komunikaty jeśli czegoś brakuje.
# nastepny etap - wprowadzenie ceny za kawę, razem z wydawaniem reszty oraz kasetki

# Zasoby
# woda = 1000 ml
# kawa = 10 porcji
# mleko = 100 ml

# opcja 1 - czarna 1 porcja kawy, 100 wody, 0 mleko
# opcja 2 - espresso 3 porcja kawy, 1 wody, 0 mleko
# opcja 3 - latte 1 porcja kawy, 100 wody, 20 mleko
# opcja 4 - capucino 50 wody 1 porcja kawy, 50 mleko

# zmienna z zasobami i petla while która się pyta co podać. Można pokazać to zarówno zmiennymi jak i listą. Lista list

oferta = [
    ['Czarna', 100, 1, 0],
    ['Espresso', 10, 3, 0],
    ['Latte', 100, 1, 20],
    ['Capucino', 50, 1, 50],
]

woda = 1000
kawa = 10
mleko = 100

n = 0

while n < len(oferta):
    print('Wybierz jedną z',len(oferta), 'pyszych kaw wpisując liczby od 0 do ',len(oferta))
    print(oferta)
    a = input('Jaką kawę przygotować? ')
    wybor = int(a)

    if wybor == 0:
        woda = woda - 100
        kawa = kawa - 1
        mleko = mleko - 0
        print(woda, kawa, mleko)

    elif wybor == 1:
        woda = woda - 10
        kawa = kawa - 3
        mleko = mleko - 0
        print(woda, kawa, mleko)

    elif wybor == 2:
        woda = woda - 100
        kawa = kawa - 1
        mleko = mleko - 20
        print(woda, kawa, mleko)

    elif wybor == 3:
        woda = woda - 50
        kawa = kawa - 1
        mleko = mleko - 50
        print(woda, kawa, mleko)

    if mleko <= 0:
        print('skończyło się mleko, możesz pić tylko czarną i espresso')
        del oferta[2]
        del oferta[2]

    print(oferta)

    n = n - 1
