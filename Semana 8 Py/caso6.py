dolar = 3.78
euro = 4.20

def convertir():
    while True:
        print("Bienvenido al convesor de monedas")
        print("\n1. Dolares")
        print("2. Euros")
        print("3. Salir")
         
        opc = int(input("Ingrese una opcion: "))

        soles = float(input("Ingrese el monto en soles: "))

        match opc:
            case 1:
                conv_d = soles/dolar
                print("\nConversion a dolar: ",round (conv_d))
            case 2:
                conv_e = soles/euro
                print("\nConversion a euros: ",round (conv_e))
            case 3:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion invalida")
                continue
        conti = input("\nDesea continuar? Presione (y): ")
        if conti != "y":
            print("\nPrograma finalizado!")
            break

convertir()