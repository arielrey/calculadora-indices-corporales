"""Nombre de la función: calcular_calorias_en_actividad
Descripción de la función: Calcula la cantidad de calorías que una persona quema al realizar algún
tipo de actividad física (esto es, su tasa metabólica basal según actividad física), a partir de la
ecuación definida anteriormente."""


def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):

    f = int(5)
    m = int(-161)

    #calificar actividad fisica segun dias
    calificar_valor_actividad(valor_actividad)

    #calcula quema de grasa segun actividad fisica
    if valor_genero == "f":
        TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + f
        TMB_actividad_fisica = TMB * valor_actividad
        print ("Usted quema", TMB_actividad_fisica ,"calorias")

        
    if valor_genero == "m":
        TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + m
        TMB_actividad_fisica = TMB * valor_actividad
        print ("Usted quema", TMB_actividad_fisica ,"calorias")



def calificar_valor_actividad(valor_actividad):    
    if valor_actividad > 1:
        valor_actividad = float(1.2)
        
    if valor_actividad >= 1 and valor_actividad <= 3:
        valor_actividad = float(1.375)
    
    if valor_actividad > 3 and valor_actividad <=5:
        valor_actividad = float(1.55)

    if valor_actividad >= 6 and valor_actividad <= 7:
        valor_actividad = float(1.72)

    if valor_actividad == 8:
        valor_actividad = float(1.9)





def interfazCaloriaActiva():
    peso = float(input("Ingresar su peso: "))
    altura = float(input("Ingresar su altura: "))
    edad = int(input("Ingresar su edad: "))
    valor_genero = input("Ingresar su genero (m/f): ")
    valor_actividad = int(input("¿Cuantos dias a la semana realiza actividad fisica? \n (ingresar '8' si realiza entrenamientos mañana y tarde): "))
    calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)