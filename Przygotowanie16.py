import random
computeroll=random.randrange(1,7)
humanroll=int(input("Podaj liczbę od 1 do 6:"))
if humanroll==computeroll:
    print(True)
else:
    print("Dureń")