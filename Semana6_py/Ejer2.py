sumaI = sumaP = 0
while True:
    num = int(input("Ingrese numero positivo (0 salir): "))

    if num < 0:
        print("Numero invalido. Ingrese numero positivo: ")
        continue
    if(num == 0):
        break

    if num%2 ==0:
        sumaP += num;
    else:
        sumaI += num;

print("\nSuma de pres: ", sumaP)
print("Suma de impares: ", sumaI)