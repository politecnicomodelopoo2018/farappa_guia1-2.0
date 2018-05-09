from Ej_7_Bufe import LasBufes
from Ej_7_Alumno import Alumno
from Ej_7_Pedido import Pedido
from Ej_7_Profesor import Profe

a = Alumno('Pedro','Alfonsin','5')
a1 = Alumno('Pedro','Raul','5')
b = Pedido(123,'12/12/12','si',None, a)
b1 = Pedido(123,'11/11/11','si',None, a1)
Buf = LasBufes()
Buf.AgregarPedidos(b)
Buf.AgregarPedidos(b1)
Buf.GuardarAlumnos()
print(Buf.Abrirlo())