from Prueba_3_Empresa import Empresa
import datetime
sony = Empresa()
sony.AgregarEmp('Pedro',2134,'Chile',1567894523)
sony.AgregarEmp('Gabriel',2154,'Peru',1569894523)
sony.AgregarEmp('Jose',2554,'Argentina',1569994523)
fecha= datetime.date(2018,2,12)
sony.Llamada('Pedro','Pedro','Gabriel',fecha,15)
sony.Llamada('Gabriel','Gabriel','Jose',fecha,15)
sony.Llamada('Gabriel','Gabriel','Pedro',fecha,15)
print(sony.Listado('Pedro'))
print(sony.Rank())
