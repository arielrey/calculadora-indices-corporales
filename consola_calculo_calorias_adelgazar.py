def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):

    m = int(5)
    f = int(-161)

    if valor_genero == "f":
        TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + f
        caloriasMin = TMB * 15 / 100
        caloriasMax = TMB * 20 / 100
        print ("Para adelgazar es recomendado que consumas entre:", caloriasMin ," y ", caloriasMax ," calorías al día.")



    if valor_genero == "m":
        TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + m
        caloriasMin = TMB * 15 / 100
        caloriasMax = TMB * 20 / 100
        print ("Para adelgazar es recomendado que consumas entre:", caloriasMin ," y ", caloriasMax ," calorías al día.")



def interfazAdelgazar():
    peso = float(input("Ingresar su peso: "))
    altura = float(input("Ingresar su altura: "))
    edad = int(input("Ingresar su edad: "))
    valor_genero = input("Ingresar su genero (m/f): ")
    consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)