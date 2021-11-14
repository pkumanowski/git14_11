# change to square pizza
cenaPizza1 = float(input("podaj cene 1 pizzy: "))
pizza1a = float(input("bok dluzszy 1 pizzy: "))
pizza1b = float(input("bok krotszy 1 pizzy: "))
cenaPizza2 = float(input("podaj cene 2 pizzy: "))
srednica2 = float(input("podaj srednice 2 pizzy: "))

pi = 3.14

promien1 = srednica1 / 2
promien2 = srednica2 / 2
pole1 = pizza1a * pizza1b
pole2 = pi * promien2 * promien2

oplacalnosc1 = pole1 / cenaPizza1
oplacalnosc2 = pole2 / cenaPizza2
print("oplacalnosce pierwszej to: ", oplacalnosc1)
print("oplacalnosce drugiej to: ", oplacalnosc2)

if oplacalnosc1 > oplacalnosc2:
    print("pierwsza pizza jest bardziej opłacalna")
elif oplacalnosc1 == oplacalnosc2:
    print("pizze sa tak samo oplacalne")
else:
    print("druga pizza jest bardziej opłacalna")
