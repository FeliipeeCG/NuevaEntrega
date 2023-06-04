class Bombilla:
    
    def __init__(self, material=None, origen=None):
        self.material = material
        self.origen = origen

    def fabricarBombilla(self, codigoBombilla, nombreBombilla):
        with open('./mates/recursos/listaBombillas.txt', 'a') as nuevaBombilla:
            data= f'{codigoBombilla}|{nombreBombilla}|{self.material}|{self.origen}|'
            nuevaBombilla.write(data)
            nuevaBombilla.close()
        return("Creamos una bombilla")

    def obtenerBombilla(self, codigoBombilla=None):
        with open('./mates/recursos/listaBombillas.txt', 'r') as Bombillas:
            for Bombilla in Bombillas:
                detalles = Bombilla.split("|")
                if codigoBombilla == detalles[0]:
                    Bombillas.close()
                    return detalles
            else:
                Bombillas.close()
                return False