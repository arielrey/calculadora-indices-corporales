import consola_calculo_imc, consola_calculo_porcentaje_grasa, consola_calculo_calorias_reposo, consola_calculo_calorias_actividad, consola_calculo_calorias_adelgazar

#interfaz para comenzar
print("\n Calculadora de Indice Corporales")
print("\n Ingresar la opcion deseada")

#opciones
print("1- Calcular IMC.")
print("2- Calcular grasa corporal.")
print("3- Calcular calorias en reposo.")
print("4- Calcular calorias en actividad.")
print("5- Consumo calorias recomendado para adelgazar.")
print("6- Salir.")

start=int(input("\nIngresar opcion: "))

match start:
    case 1:
        consola_calculo_imc.interfazIMC()
    case 2:
        consola_calculo_porcentaje_grasa.interfazPorcGrasa()
    case 3:
        consola_calculo_calorias_reposo.interfazCaloriasReposo()
    case 4:
        consola_calculo_calorias_actividad.interfazCaloriaActiva()
    case 5:
        consola_calculo_calorias_adelgazar.interfazAdelgazar()
    case 6:
        print("\nHasta pronto!")

if start <= 0 or start > 6:
    print ("\n Opcion invalida.")