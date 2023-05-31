def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    
    m = float(10.8)
    f = float(0)
    imc = peso / (altura*altura)


#calcular %GC segun genero y recomendaciones por edades
    #masculino
    if valor_genero == "m":
        
        porcentajeGrasa = 1.2 * imc + 0.23 * edad - 5.4 - m
        print ("Su porcentaje de grasa es: ", porcentajeGrasa)


        #calcular recomendaciones entre 20 a 29 años
        if edad >=20 and edad <= 29 and porcentajeGrasa >= 11 and porcentajeGrasa <= 20:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=20 and edad <= 29 and porcentajeGrasa < 11:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=20 and edad <= 29 and porcentajeGrasa > 20:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")


        #calcular recomendaciones entre 30 a 39 años
        if edad >=30 and edad <= 39 and porcentajeGrasa >= 12 and porcentajeGrasa <= 21:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=30 and edad <= 39 and porcentajeGrasa < 12:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=30 and edad <= 39 and porcentajeGrasa > 21:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")


        #calcular recomendaciones entre 40 a 49 años
        if edad >=40 and edad <= 49 and porcentajeGrasa >= 18 and porcentajeGrasa <= 30:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=40 and edad <= 49 and porcentajeGrasa < 18:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=40 and edad <= 49 and porcentajeGrasa > 30:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")


        #calcular recomendaciones entre 50 a 59 años
        if edad >=50 and edad <= 59 and porcentajeGrasa >= 19 and porcentajeGrasa <= 31:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=50 and edad <= 59 and porcentajeGrasa < 19:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=50 and edad <= 59 and porcentajeGrasa > 31:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")



    #femenino
    if valor_genero =="f":
        
        porcentajeGrasa = 1.2 * imc + 0.23 * edad - 5.4 - f
        print ("Su porcentaje de grasa es: ", porcentajeGrasa)

        #calcular recomendaciones entre 20 a 29 años
        if edad >=20 and edad <= 29 and porcentajeGrasa >= 16 and porcentajeGrasa <= 28:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=20 and edad <= 29 and porcentajeGrasa < 16:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=20 and edad <= 29 and porcentajeGrasa > 28:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")


        #calcular recomendaciones entre 30 a 39 años
        if edad >=30 and edad <= 39 and porcentajeGrasa >= 17 and porcentajeGrasa <= 29:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=30 and edad <= 39 and porcentajeGrasa < 17:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=30 and edad <= 39 and porcentajeGrasa > 29:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")


        #calcular recomendaciones entre 40 a 49 años
        if edad >=40 and edad <= 49 and porcentajeGrasa >= 18 and porcentajeGrasa <= 30:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=40 and edad <= 49 and porcentajeGrasa < 18:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=40 and edad <= 49 and porcentajeGrasa > 30:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")


        #calcular recomendaciones entre 50 a 59 años
        if edad >=50 and edad <= 59 and porcentajeGrasa >= 19 and porcentajeGrasa <= 31:
            print ("Su cuerpo contiene la grasa recomendada (porcentaje entre 11 a 20) segun su edad. ")
        if edad >=50 and edad <= 59 and porcentajeGrasa < 19:
            print ("Su porcentaje de grasa corporal esta por lo bajo de lo recomendado. ")
        if edad >=50 and edad <= 59 and porcentajeGrasa > 31:
            print ("Su porcentaje de grasa corporal supera a lo recomendado. ")





def interfazPorcGrasa():

    peso = float(input("Ingresar su peso corporal: "))
    altura = float(input("Ingresar su altura: "))
    edad = int(input("Ingresar su edad: "))
    valor_genero = input("Ingresar su genero (m/f): ")
    calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
