from Class import Alumno
import datetime
a= Alumno()
a.setNombre("Pedro")
a.setApellido("Benedetto")
fecha = datetime.date(2000,10,22)
a.setFechaNac(fecha)
a.AgregarNota(10)
mayor = a.mayorNota()
if mayor:
print(mayor)