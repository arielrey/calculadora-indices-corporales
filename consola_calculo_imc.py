def calcular_IMC(pesoInp, alturaInp):
    
    #calcular IMC
    imc = pesoInp / (alturaInp*alturaInp)
    print("Su IMC es: ", imc)
    
    #clasificar imc
    clasificarIMC(imc)


def clasificarIMC(imc):

    if imc < float(16.00):
        print ("Delgadez Severa")
    
    if imc >= float(16.00) and imc <= float(16.99):
        print ("Delgadez Moderada")
    
    if imc >= float(17.00) and imc < float(18.49):
        print("Delgadez aceptable")

    if imc >= float(18.5) and imc < float(24.99):
        print("Peso Normal")

    if imc >= float(25.00) and imc <= float(29.99):
        print("Sobrepeso")
    
    if imc >= float(30.00) and imc <= float(34.99):
        print ("Obesidad tipo I")
    
    if imc >= float(35.00) and imc <= float(39.99):
        print("Obesidad tipo II")

    if imc >= float(40.00) and imc <= float(49.99):
        print("Obesidad tipo III o morbida")
    
    if imc >= float(50.00):
        print("Obesidad tipo IV o extrema")




def interfazIMC():

    pesoInp = float(input("Ingresar su peso corporal: "))
    alturaInp = float(input("Ingresar su altura: "))

    calcular_IMC(pesoInp, alturaInp)

