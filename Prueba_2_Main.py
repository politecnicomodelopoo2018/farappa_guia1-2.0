from Familia import Family
import datetime
Fam = Family()
Fecha = datetime.date(1995,5,10)
Fam.AgregarPersona('Pedro',Fecha)
Fam.AgregarPersona('Ruben',Fecha)
Fam.AgregarPlato('Pedro','Papas',40)
Fam.AgregarPlato('Pedro','Caca',100)
Fam.AgregarPlato('Ruben','Papas',300)
Fam.AgregarPlato('Ruben','Caca',1000)
print(Fam.CantCalo('Pedro'))
print(Fam.Prom())
print(Fam.Max())
print(Fam.Min())