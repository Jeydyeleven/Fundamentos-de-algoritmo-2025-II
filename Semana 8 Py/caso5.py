def sumar (a, b):
    print("\nLa suma es: ", a + b)

def resta(a, b):
    print("\nLa resta es: ", a - b)

def multi(a, b):
    print("\nLa multiplicacion es: ", a * b)

def divi(a, b):
   if b != 0:
        print("\nLa division es: ", a / b)
   else: print("No se puede dividir por cero")

def operaciones():
    while True:
        print("Bienvenido a sistema de operaciones")
        print("1. Suma")
        print("2. Resta")    
        print("3. Multiplicacion")
        print("4. Division")

        opc = int(input("\nSeleccione una opcion: "))

        a = int(input("\nIngrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))

        match opc:
            case 1: sumar(a, b)
            case 2: resta(a, b)
            case 3: multi(a, b)
            case 4: divi(a, b)
            case _:
                print("Opcion invalida")
                continue
        conti = input("\Desea continuar? Presione (y): ")

        if conti != "y":
            print("\nPrograma finalizado!")
            break
operaciones()