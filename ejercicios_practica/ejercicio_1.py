# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones
def ingreso_numero():
    numero = int(input("Ingrese un número: "))
    return numero

    # En esta función debe determinar cual de los dos
    # números ingresados por parámetro es mayor
    # y luego imprimir dicho valor en pantalla
def imprimir_mayor(numero_1, numero_2):
    print("Funcion imprimir mayor")
    if numero_1 > numero_2:
        print("El mayor de {} y {} es {}".format(numero_1,numero_2,numero_1))
    elif numero_2 > numero_1:
        print("El mayor de {} y {} es {}".format(numero_1,numero_2,numero_2))
    else:
        print("Los números son iguales y su valor es:  {}".format(numero_1))



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numero_1 = ingreso_numero()
    numero_2 = ingreso_numero()
    # Alumno: Complete la función "imprimir_mayor"
    imprimir_mayor(numero_1,numero_2)

    print("terminamos")