def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    f = int(5)
    m = int(-161)
    if valor_genero == "f":
        TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + f
        print ("Su cantidad de calorías que quema en reposo: ", TMB)
    if valor_genero == "m":
        TMB = (10 * peso) + (6.25 * altura) - (5 * edad) + m
        print ("Su cantidad de calorías que quema en reposo: ", TMB)

def interfazCaloriasReposo():
    peso = float(input("Ingresar su peso: "))
    altura = float(input("Ingresar su altura: "))
    edad = int(input("Ingresar su edad: "))
    valor_genero = input("Ingresar su genero (m/f): ")
    calcular_calorias_en_reposo(peso, altura, edad, valor_genero)