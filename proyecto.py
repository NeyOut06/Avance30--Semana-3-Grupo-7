import random

def main():
        while True:
            n = int(input("Ingrese el numero de elementos para el conjunto A (entre 4 y 7): "))
            if 4 <= n <= 7:
                print(f"El numero {n} esta dentro del rango permitido :)\n")
                break  #sale del bucle si no esta en el rango
            else:
                print("El numero de elementos debe estar entre 4 y 7. Intentalo nuevamente :( .\n")
        

        #se ingresará los elementos necesariamente entre 1 y 12
        conjunto_a = set() #se crea un conjunto vacio
        for i in range(n): #recorre n veces pidiendo los elementos por n veces
             while True:
                elemento = int(input(f"Ingrese el elemento {i+1} (entre 1 y 12): "))
                if 1 <= elemento <= 12:
                    conjunto_a.add(elemento)  #agrega el elemento al conjunto
                    break  # Sale si el elemento está dentro del rango si no repite hasta que coloque un elemento valido
                else:
                    print("El elemento debe estar entre 1 y 12. Intentalo nuevamente.")

        #definimos la lista de valores de m y el conjunto vacio de la relacion r 
        valores_m = [3, 4, 5, 6]
        relacion_r = set()
        for x in conjunto_a:
            for y in conjunto_a:
                if (x + y) % valores_m[0] == 0 or (x + y) % valores_m[1] == 0 or (x + y) % valores_m[2] == 0 or (x + y) % valores_m[3] == 0: #verifica si es multiplo de algun elemento de la lista m
                    relacion_r.add((x, y)) 

        #verifica si la relación R es reflexiva, simétrica y transitiva, bota true si es que cumple
        reflexiva = all((x, x) in relacion_r for x in conjunto_a)  #devuelve true si todos los elementos son verdaderos y false si al menos uno es falso
        simetrica = all((y, x) in relacion_r for x, y in relacion_r)
        transitiva = all((x, z) in relacion_r for x, y in relacion_r for y2, z in relacion_r if y == y2)

        print("Elementos de R por extension:")
        print(relacion_r) #muestra los elementos del conjunto relacion_r por extension

        print("\nElementos de R en matriz:")
        matriz_r_lista = [] #creamos una lista vacia para crear una matriz fila por fila
        for x in conjunto_a:
            row = [1 if (x, y) in relacion_r else 0 for y in conjunto_a] #coloca 1 si las componentes estan en el conjunto relacion r y 0 si no
            matriz_r_lista.append(row)
        for row in matriz_r_lista: 
            print(row)
        
        print("\nPropiedades de R:") #nos indicara las propiedades de R
        if reflexiva==True:
            print('La relacion si es reflexiva')
        else:
            print('La relacion no es reflexiva')
        if simetrica==True:
            print('La relacion si es simetrica')
        else:
            print('La relacion no es simetrica')
        if transitiva==True:
            print('La relacion si es transitiva')
        else:
            print('La relacion no es transitiva')

    
main()
