wysokość=int(input("Wpisz swój wzrost w centymetrach:"))
overallinches=round(wysokość/2.54)
feet=overallinches//12
inches=overallinches%12
print(f"Twoja wysokość wynosi {feet} feet i {inches} inches")