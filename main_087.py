from funciones import *


def menu():
    print("\n==============================================MENÚ======================================================")
    print("1. Crear Archivo Binario desde archivo .csv. SIEMPRE DESDE CERO")
    print("2. Cargar por teclado los datos de un ticket en un achivo binario")
    print("3. Mostrar todos los registros del Archivo Binario")
    print("4. Mostrar Todos los registros cuya patente sea igual a una cargada por teclado")
    print("5. Buscar si existe un registro por código de ticket")
    print("6. Determinar y buscar la cantidad de combinaciones posibles entre tipo de veíchulo y país de cabina")
    print("7. Mostrar el TOTAL de tickets contados por cada tipo de vehiculos y país de cabiba")
    print("8. Calcular y mostrar la distancia promedio desde la última cabina entre todos los vehículos")
    print("9. Salir")
    print("=========================================================================================================\n")


def main():
    menu()
    fd = "tickets.dat"
    op = -1
    while op != 9:
        op = validar_rango(1, 9, "\n------> Ingrese una opción del menú: ")
        if op == 1:
            tf = "peajes-tp4.csv"
            res = input("\n¡¡¡ADVERTENCIA:La opción eliminara los datos del arreglo!!!."
                        "\n\n¿Desea continuar? S.(Continuar)/N.(Volver al menú): ").lower()
            if res == "s":
                crear_archivo_auto(tf, fd)
                print()
            elif res == "n":
                print("\nFue re dirigido al menú nuevamente\n")
            else:
                print("\nNo ingreso una opción valida para continuar.Fue re dirigido al menú.\n")
        elif op == 2:
            carga_manual_archivo(fd)
        elif op == 3:
            mostrar_archivo(fd)
        elif op == 4:
            m = open(fd, 'rb')
            p = input("Ingresar la patente del vehículo que desee filtrar: ").upper().strip()
            filtrar_patentes(fd, m, p)
        elif op == 5:
            c = int(input("Ingresar el código de ticket a buscar: "))
            m = open(fd, "rb")
            encontrado = buscar_codigo(fd, m, c)
            if encontrado:
                print(mostrar_encabezado())
                print(encontrado)
            else:
                print("\nNo se ha encontrado el ticket\n")
        elif op == 6:
            print(f'{"-"*70}\n{"TIPO DE VEHÍCULO":^22} | {"PAÍS DE LA CABINA":^22} | {"CANTIDAD":^20} \n{"-"*70}')
            mostrar_matriz_conteo(fd)
        elif op == 7:
            totalizar_cabinas_tipo(fd)
        elif op == 8:
            v = crear_vector_mayores_promedio(fd)
            shell_sort(v)
            contador = 0
            for ticket in v:
                contador += 1
                print(ticket)
            prom = calcular_promedio_distancias(fd)
            print(f'\nLa distnacia promedio de km recorridos de todos los vehículos es: {round(prom, 2)}km')
            print(f'La cantidad de tickets que superan el promedio de kilometros recorridos es de: {contador}')
        elif op == 9:
            print("\n--------Gracias por utilizar la gestión de Cabinas de Peaje 4.0---------")


if __name__ == "__main__":
    main()