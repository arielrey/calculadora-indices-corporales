"""
Descripción de la función: Calcula el porcentaje de grasa de una persona a partir de la ecuación
definida anteriormente.

Parámetros y retorno:
Nombre Tipo Descripción
peso float Peso de la persona en kilogramos.
altura float Altura de la persona en metros.
edad int Edad de la persona en años.
valor_genero float Valor que varía según el género de la persona: en caso de ser masculino debe

ser 10.8 y en caso de ser femenino debe ser 0.
Retorno float El porcentaje de grasa que tiene el cuerpo de la persona.


"""


def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    
    m = float(10.8)
    f = float(0)
    imc = peso / (altura*altura)

    if valor_genero == "m":
        porcentajeGrasa = 1.2 * imc + 0.23 * edad - 5.4 - m
        print ("Su porcentaje de grasa es: ", porcentajeGrasa)
    if valor_genero =="f":
        porcentajeGrasa = 1.2 * imc + 0.23 * edad - 5.4 - f
        print ("Su porcentaje de grasa es: ", porcentajeGrasa)




def interfazPorcGrasa():

    peso = float(input("Ingresar su peso corporal: "))
    altura = float(input("Ingresar su altura: "))
    edad = int(input("Ingresar su edad: "))
    valor_genero = input("Ingresar su genero (m/f): ")
    calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
