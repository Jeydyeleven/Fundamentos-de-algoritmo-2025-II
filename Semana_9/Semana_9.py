from triangulo import triangulo
c = triangulo()

def menu1() -> None:
    print("BIENVENIDOS AL CALCULO DE AREA Y PERIMETROS")
    print("********Menu de opciones*********")
    print("*     1.Triangulo               *")
    print("*     2.Cuadrado                *")
    print("*     3.Rectangulo              *")
    print("*     4.Trapecio                *")
    print("*     0.Salir                   *")
    print("*******************************\n")

def menu2() -> int:
    print("********************")
    print("*    1.Area        *")
    print("*    1.Perimetro   *")
    print("******************\n")

    opcion2 = int(input("Ingrese opcion: "))
    return opcion2

while True:
    menu1()
    while True:
        opcion = int(input("Ingrese opcion: "))
        if opcion in (0,1,2,3,4):
            break
        else: print("Opcion no valida. Ingrese nuevamente.\n")

    match opcion:
        case 0: quit() #exit()
        case 1: 
            opc2 = menu2()
            match opc2:
                case 1: t.area()
                case 2: t.perimetro()

        case 2: print()
        case 3: print()
        case 4: print()

    while True:
        conti = input("\n¿Desea continuar? (s/n): ")
        if conti in("s", "n"): break
        else: print("Error. Presione solo 's' o 'n'. ")

    if conti =="n": break