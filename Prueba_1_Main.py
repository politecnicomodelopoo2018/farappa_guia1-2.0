from Prueba_1_Persona import Persona
import datetime

a=Persona('Pedro','Alvarez',datetime.date(1990,5,2))
peso=75
altura=1.89
fecha=datetime.date(2018,5,2)
a.agregarMedidas(peso,altura,fecha)
print(a.caca())
print(a.VerSegunFedeFer(fecha))
