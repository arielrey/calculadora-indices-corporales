"""Trabajo Pactico #1 Programacion II
Nombre de la función: calcular_IMC
Nombre de la función: calcular_porcentaje_grasa
Nombre de la función: calcular_calorias_en_reposo
Nombre de la función: calcular_calorias_en_actividad
Nombre de la función: consumo_calorias_recomendado_para_adelgazar
"""

import consola_calculo_imc, consola_calculo_porcentaje_grasa

#interfaz para comenzar
print("\n Calculadora de Indice Corporales")
print("\n Ingresar la opcion deseada")

#opciones
print("1- Calcular IMC.")
print("2- Calcular grasa corporal.")
print("3- Calcular calorias en reposo.")
print("4- Calcular calorias en actividad.")
print("5- Salir.")

start=int(input("\nIngresar opcion: "))

match start:
    case 1:
        consola_calculo_imc.interfazIMC()
    case 2:
        consola_calculo_porcentaje_grasa.interfazPorcGrasa()
    case 3:
        print("\nElegiste 3")
    case 4:
        print("\nElegiste 4")
    case 5:
        print("\nElegiste 5")

if start <= 0 or start > 5:
    print ("\n Opcion invalida.")