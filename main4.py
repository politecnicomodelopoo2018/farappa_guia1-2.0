from Empresa import Empresa
import datetime
Sony = Empresa()

fecha = datetime.date(1990,10,20)
Sony.AgregarEmpleado('Pedro','Ramirez','15 5566-7745',fecha)


print(Sony.VerPromMes('Pedro',2018,10))