from Prueba_3_Empleado import Empleado
class Empresa(object):

    def __init__(self):
        self.listaEmp=[]

    def AgregarEmp(self,Nombre,DNI,Pais,Nro):
        Emp=Empleado(Nombre,DNI,Pais,Nro)
        self.listaEmp.append(Emp)
    def Listado(self,Nombre):
        for a in self.listaEmp:
            if a.Nombre == Nombre:
                for b in a.ListaLlamadas:
                    return b.Emisor,b.Receptor,b.Fecha,b.Duracion

    def Llamada(self,Nombre,Em,Re,fecha,dur):
        for a in self.listaEmp:
            if a.Nombre == Nombre:
                a.AgregarLlamada(Em,Re,fecha,dur)

    def Rank(self):
        j=None
        Empleados=[]
        Exterior=[]
        for a in self.listaEmp:
            if a.Pais is not 'Argentina':
                Empleados.append(a)
        for a in self.listaEmp:
            for b in a.ListaLlamadas:
                j=b.Receptor
                for y in Empleados:
                    if j == y.Nombre:
                        Exterior.append(a.Nombre)
        return Exterior


