import os
import random
from collections import OrderedDict
#resaltar diagonal unicamente verde
def resaltar_diagonal(R, A):
    print("\nMatriz graficada del conjunto R:\n")
    print("  ", end="")
    for x in A:
        print(f"{x:2}", end="")
    print()

    for x in A:
        print(f"{x:2}", end=" ")
        for y in A:
            if x == y:  # Verificar si es un elemento de la diagonal
                print(f"\033[32m{1 if (x, y) in R else 0}\033[0m", end=" ")  # Imprimir en verde
            else:
                print("1" if (x, y) in R else "0", end=" ")
        print()
#funcion para resaltar la diagonal verde y rojo de una matriz
def resaltar_diagonal_vyr(R, A):
    print("\nMatriz graficada del conjunto R:\n")
    print("  ", end="")
    for x in A:
        print(f"{x:2}", end="")
    print()

    for x in A:
        print(f"{x:2}", end=" ")
        for y in A:
            if x == y:  # Verificar si es un elemento de la diagonal
                if (x, y) in R:
                    print(f"\033[32m1\033[0m", end=" ")  # Imprimir 1 en verde
                else:
                    print(f"\033[31m0\033[0m", end=" ")  # Imprimir 0 en rojo
            else:
                print("1" if (x, y) in R else "0", end=" ")  # Sin colores para los elementos fuera de la diagonal
        print()
# Funcion para generar un conjunto aleatorio de enteros
def generar_conjunto(n):
    conjunto = set()
    while len(conjunto) < n:
        elemento = random.randint(1, 12)
        conjunto.add(elemento)
    return conjunto

# Funcion para definir la relacion R
def relacion_R(A):
    R = OrderedDict()
    for x in A:
        for y in A:
            suma = x + y
            if suma % 3 == 0 or suma % 4 == 0 or suma % 5 == 0 or suma % 6 == 0:
                R[(x, y)] = True
    return R

# Funcion para verificar si una relacion es reflexiva
def es_reflexiva(R, A):
    for x in A:
        if (x, x) not in R:
            return False
    return True

# Funcion para verificar si una relacion es simetrica
def es_simetrica(R):
    for par in R:
        x, y = par
        if (y, x) not in R:
            return False
    return True

# Funcion para verificar si una relacion es transitiva
def es_transitiva(R, A):
    for x in A:
        for y in A:
            for z in A:
                if (x, y) in R and (y, z) in R and (x, z) not in R:
                    return False
    return True

# Funcion para obtener las clases de equivalencia
def clase_equivalencia(x, A, R):
    clase = set()
    for y in A:
        if (x, y) in R and (y, x) in R:
            clase.add(y)
    return clase

# Funcion para imprimir la matriz graficada de la relacion
def imprimir_matriz(R, A):
    print("\nMatriz graficada del conjunto R:\n")
    print("  ", end="")  # Imprimir un solo espacio en blanco
    for x in A:
        print(f"{x:2}", end="")  # Formatear con ancho de 2 sin espacios adicionales
    print()  # Imprimir una nueva línea

    for x in A:
        print(f"{x:2}", end=" ")  # Formatear con ancho de 2 y un espacio al final
        for y in A:
            if (x, y) in R:
                print("1", end=" ")  # Sin espacios adicionales
            else:
                print("0", end=" ")  # Sin espacios adicionales
        print()  # Imprimir una nueva línea

def mostrar_titulo_pantalla_inicio():
    # Título
    print("\033[34m", end="")  # Cambiar color de texto a rojo
    print(" ______         _           _         ______              _        _")
    print("|__  __|       | |         (_)       |   __ \\            (_)      | |")
    print("  |  |_ __ __ _| |__   __ _ _  ___   |  |__) |_ _ _ __ __ _   __ _| |")
    print("  |  |'__/  _' | '_ \\ / _' | |/ _ \\  |   ___/ _' | '_/  _| |/  _' | |")
    print("  |  | | | (_| | |_) | (_| | | (_) | |  |  | (_| | | | (_| |  (_| | |")
    print("  |__|_|  \\__,_|_.__/ \\__,_| |\\___/  |__|   \\__,_|_| \\___|_|\\__,__|_|")
    print("                          _/ |")
    print("                         |__ /")
    print("\033[0m", end="")  # Restablecer color de texto
    # Pantalla de inicio
    print("\033[31m", end="")  # Cambiar color de texto a rojo
    print("\n   UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS")
    print("             Matematica Discreta")
    print("                SECCION: SI39")
    print("       PROFESOR: Jonathan Abrahan Sueros Zarate")
    print("                   INTEGRANTES:")
    print("         Kevin Rene Coronado Gonzales ")
    print("            Gian Marco Chávez López  ")
    print("            Yazid Amir Tinoco Torres ")
    print("         Anderson Yamir Olivares Polar")
    print("\033[0m", end="")  # Restablecer color de texto

def menu_principal():
    mostrar_titulo_pantalla_inicio()
    input("Presiona Enter para continuar...")
    os.system('cls')
    continuar = True
    R=None
    while continuar:
        os.system('cls')  # Limpiar la pantalla 
        print("\033[31m", end="")
        print(" ____      _            _                       ")
        print("|  _ \\ ___| | __ _  ___(_) ___  _ __   ___  ___ ")
        print("| |_) / _ \\ |/ _` |/ __| |/ _ \\| '_ \\ / _ \\/ __|")
        print("|  _ <  __/ | (_| | (__| | (_) | | | |  __/\\__ \\")
        print("|_| \\_\\___|_|\\__,_|\\___|_|\\___/|_| |_|\\___||___/")
        print("=====================")
        print("Tema A1")
        print("\033[32mMenu:\033[0m")
        print("1. Formar conjunto A, AxA y R (con su restriccion), imprimiendo la matriz de R")
        print("2. Saber si R es reflexiva")
        print("3. Saber si R es simetrica")
        print("4. Saber si R es transitiva")
        print("5. Saber si R es equivalencia")
        print("6. Salir")
        opcion = input("\nPor favor, selecciona una opcion: ")

        if opcion == '1':
            os.system('cls')  # Limpiar la pantalla
            n=0 
            while n < 4 or n > 7:
                n = int(input("Ingrese el tamano del conjunto A (entre 4 y 7): "))
            opcion_conjunto=""
            while opcion_conjunto!="SI" and opcion_conjunto!="NO":
                opcion_conjunto = input("\nDesea ingresar los elementos del conjunto A (si) o generarlos aleatoriamente (no)? ").upper()
            if opcion_conjunto == "NO":
                A = generar_conjunto(n)
                os.system("cls")
                print("Elementos del conjunto A generado aleatoriamente:", A)
            if opcion_conjunto == "SI":
                A = OrderedDict()
                print("\nIngrese los elementos del conjunto A (entre 1 y 12):")
                for i in range(n):
                    elemento=0
                    while elemento < 1 or elemento > 12:
                        elemento = int(input(f"Elemento {i+1}: "))                   
                    A[elemento] = True
                A = list(A.keys())
                os.system("cls")
                print("Conjunto A ingresado:", A)
            

            R = relacion_R(A)
            print("Elementos Relacion R:", list(R.keys()))
            print(" __________________________________________________________________________________")
            print("| Un par ordenado (x, y) pertenece a R si la suma x + y es multiplo de 3, 4, 5 o 6.|")
            print("|__________________________________________________________________________________|\n")
            imprimir_matriz(R, A)
            input("Presiona Enter para continuar...")
        elif opcion in ['2', '3', '4', '5']:
            if R is None:
                print("Debe crear un conjunto primero.")
                input("Presiona Enter para continuar...")
            else:
                if opcion == '2':
                    os.system('cls')  # Limpiar la pantalla           
                    print("La relacion R es reflexiva?")
                    print(" _____________________________________________")
                    print("| Reflexiva <=> [(a, a) E R, para todo a E A] |")
                    print("|_____________________________________________|")
                    print("\nEs decir, si en la diagonal hay solament 1's es reflexiva, caso contrario no lo es")
                    opc=es_reflexiva(R,A)
                    resaltar_diagonal_vyr(R,A)
                    if opc==True:
                        print("\n La relación es reflexiva, su diagonal son unicamente 1's")
                    elif opc==False:
                        print("\nLa relación R no es reflexiva, su diagonal no son unicamente 1's")
                    input("Presiona Enter para continuar...")

                elif opcion == '3':
                    os.system('cls')  # Limpiar la pantalla 
                    print("La relacion R es simetrica?")
                    print(" ______________________________________________________________")
                    print("| Simetrica <=> [(a, b) E R => (b, a) E R, para todo a, b E A] |")
                    print("|______________________________________________________________|")
                    print("\nEs decir, si los elementos equidistantes de la diagonal son iguales, es simetrica")
                    opc=es_simetrica(R)
                    resaltar_diagonal(R,A)
                    if opc==True:
                        print("\n La relación SI es simetrica, los elementos equidistantes son iguales")
                    elif opc==False:
                        print("\nLa relación R NO es simetrica, los elementos equidistantes no son iguales")
                    input("Presiona Enter para continuar...")

                elif opcion == '4':
                    os.system('cls')  # Limpiar la pantalla 
                    print("La relacion R es transitiva?")
                    print(" _______________________________________________________________________________")
                    print("| Transitiva <=> [(a, b) E R y (b, c) E R => (a, c) E R, para todo a, b, c E A] |")
                    print("|_______________________________________________________________________________|")
                    print("\nEs decir, si los pares (a,b) y (b,c) están en la relación, el par ordenado (a,c), también tiene que estar")
                    opc=es_transitiva(R,A)
                    imprimir_matriz(R, A)
                    if opc==True:
                        print("\n La relación SI es Transitiva, se cumple la condición")
                    elif opc==False:
                        print("\nLa relación NO es Transitiva,  la condición no se cumple")
                    input("Presiona Enter para continuar...")

                elif opcion == '5':
                    os.system('cls')  # Limpiar la pantalla 
                    print("R es una relacion de equivalencia?")
                    print(" ________________________________________________________________")
                    print("| Relacion de Equivalencia <=> Reflexiva, Simetrica y Transitiva |")
                    print("|________________________________________________________________|")
                    print("\nEs decir, si la relacion es reflexiva, simetrica y transitiva, esta sera una relacion de equivalencia")
                    imprimir_matriz(R, A)
                    print("\n")
                    if(es_reflexiva(R,A)):
                        print("SI es una relacion Reflexiva")
                    else:
                        print("NO es una relacion reflexiva")
                    if(es_simetrica(R)):
                        print("SI es una relacion Simetrica")
                    else:
                        print("NO es una relacion Simetrica")
                    if(es_transitiva(R,A)):
                        print("SI es una relacion Transitiva")
                    else:
                        print("NO es una relacion Transitiva")

                    if es_reflexiva(R, A) and es_simetrica(R) and es_transitiva(R, A):
                        print("\nPor lo tanto, R es una relacion de equivalencia.\n")
                        for x in A:
                            clase = clase_equivalencia(x, A, R)
                            print(f"La clase de equivalencia del elemento {x} es: {clase}")
                    else:
                        print("Por lo tanto, R no es una relacion de equivalencia.")
                    input("Presiona Enter para continuar...")

        elif opcion == '6':
            print("Nos vemos pronto!")
            continuar = False

        else:
            print("Opcion no valida. Por favor, selecciona una opcion del 1 al 7.")
            input("Presiona Enter para continuar...")

menu_principal()
