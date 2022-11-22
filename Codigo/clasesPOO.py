
class Estado():
    
    def __init__(self, nombre):
        self.nombre = nombre

class Tipo_de_productor():
    
    def __init__(self, nombreProductor):
        self.nombreProductor = nombreProductor


class Fuente_de_energia():
    
    def __init__(self, nombreFuenteEnergia):
        self.nombreFuenteEnergia = nombreFuenteEnergia

class Energia_generada():
    
    def __init__(self, totalEnergiaGenerada, year, mes):
        self.totalEnergiaGenerada = totalEnergiaGenerada
        self.year = year
        self.mes = mes

class Estado_Productor():
    
    def __init__(self, productor:Tipo_de_productor, estado:Estado):
        self.productor = productor
        self.estado = estado

class Productor_FuenteEnergia():

    def __init__(self, productor:Tipo_de_productor, tipoEnergia:Fuente_de_energia):
        self.productor = productor
        self.tipoEnergia = tipoEnergia

if __name__ == "__main__":
    print("POO yes")
