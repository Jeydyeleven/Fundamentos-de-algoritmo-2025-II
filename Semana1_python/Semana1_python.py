def ejer1():
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")

    print(f"\n{nombre}, bienvenido al curso de algoritmo de la carrera {carrera}")
def ejer2():
    print("\"Jeyson\"")

def ejer3():
    num1= int(input("Ingrese numero 1: "))
    num2= int(input("Ingrese numero 2: "))

    print("Suma: ",(num1+num2))
    print("resta: ",(num1-num2))
    print("multiplicacion: ",(num1*num2))
    print("division: ",(num1/num2))
    
import math 
def ejer4():
    num = float(input("Ingrese numero decimal: "))

    raiz = math.sqrt(num)
    redo = round(num,2)
    cubo = math.pow(num,3)
    cubica = num ** (1/3)
    print("Raiz cuadra: ",raiz)
    print("redondeado: ",redo)
    print("al cubo: ", cubo)
    print("raiz cubica: ", cubica)
    
def ejer5():
    num = input("Ingrese un numero: ")

    entero = int(num)
    decim = float(num)

    print("Resto: ", (entero%2))
    print("Decimal: ", (decim/3))

ejer5()