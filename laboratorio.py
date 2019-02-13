class Laboratorio():
    def __init__(self, nombre, inventario):
        self.nombre = nombre
        self.inventario = inventario
    def get_nombre(self):
        return self.nombre
    def get_inventario(self):
        return self.inventario

class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio= precio

    def informacionprod(self):
        return self.nombre, self.precio

class Medicamento(Producto):
    def __init__(self, nombre, precio, sustancia, porcentaje):
        self.sustancia= sustancia
        self.porcentaje = porcentaje

    def dimeinformacion(self):
        return self.sustancia, self.porcentaje

prod1 = Producto("Gasas", 0.55)
prod2 = Producto("Agujas", 0.35)
medi1 = Medicamento("Ibuprofeno", 1.25, "Acido", 3)
medi2 = Medicamento("Aspirina", 2.20, "Ácido", 15)
invent = [prod1, prod2, medi1, medi2]
Lab = Laboratorio("Labs", invent)
