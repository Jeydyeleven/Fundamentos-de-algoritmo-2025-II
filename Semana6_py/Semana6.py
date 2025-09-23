num = int(input("Ingrese numero de la tabla: "))

while num <= 0:
    num = int(input("Numero invalido: Ingrese numero de la tabla: "))

i=1
print()
while i <=12:
    print(f"{num} x {i} = {num*1}")
    i+=1
