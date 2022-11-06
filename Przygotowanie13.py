a=int(input("Podaj pierwszy bok:"))
b=int(input("Podaj drugi bok:"))
c=int(input("Podaj trzeci bok"))
p=(a+b+c)/2
area=int((p*(p-a)*(p-b)*(p-c))**0.5)
print(area)