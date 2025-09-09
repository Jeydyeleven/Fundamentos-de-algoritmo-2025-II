using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SEMANA_1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            ejer4();
            Console.ReadKey(); //detenimiento de consola
        }
        static void ejer1()
        {
            string nombre, carrera;

            Console.Write("Ingrese su nombre :");
            nombre = Console.ReadLine();

            Console.Write("Ingrese su carrera .");
            carrera = Console.ReadLine();

            Console.WriteLine($"\n{nombre}, bienvenido al curso" + $"de fundamentos de algoritmo de la carrera {carrera}");
        }
        static void ejer2()
        {
            Console.WriteLine("\"Jeyson\"");
        }
        static void ejer3()
        {
            Console.Write("Ingrese numero 1: ");
            int num1 = int.Parse(Console.ReadLine());

            Console.Write("Ingrese numero 2: ");
            int num2 = int.Parse(Console.ReadLine());
            double divi = (double)num1 / (double)num2;

            Console.WriteLine("Suma: " + (num1 + num2));
            Console.WriteLine("Resta: " + (num1 - num2));
            Console.WriteLine("Multiplicacion: " + (num1 * num2));
            Console.WriteLine("Division: " + divi);
        }
        static void ejer4()
        {
            Console.Write("Ingrese un numero decimal: ");
            double num = double.Parse(Console.ReadLine());

            double raiz = Math.Sqrt(num);
            double redo = Math.Round(num, 2);
            double cubo = Math.Pow(num, 3);
            double cubica = Math.Pow(num, 1 / 3d);

            Console.WriteLine("Raiz cuadrada: " + raiz);
            Console.WriteLine("Redondeado; " + redo);
            Console.WriteLine("Elevado a 3: " + cubo);
            Console.WriteLine("Raiz cubica: " + cubica);
        }
        static void ejer5()
        {

        }
        static void ejer6()
        {

        }
    }
}
