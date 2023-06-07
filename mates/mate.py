from mates.bombilla import Bombilla


class Mate(Bombilla):
    def __init__(self, capacidad=None, tipo=None):
        self.capacidad = capacidad
        self.tipo = tipo

    def fabricarMate(self, codigoMate, nombreMate, codigoBombilla):
        self.codigoBombilla = codigoBombilla
        myBombilla = Bombilla()
        bombilla1 = myBombilla.obtenerBombilla(self.codigoBombilla)

        with open('./mates/recursos/listaMates.json', 'a') as nuevoMate:
            data = f'{codigoMate}|{nombreMate}|{self.tipo}|{self.capacidad}|{bombilla1[0]}|'
            nuevoMate.write(data)
            nuevoMate.close()
        print("Creamos un buen mate :)")

    def comprarMate(self, tipo):
        self.listarMates(tipo)
        seleccion = input("Seleccionar codigo de Mate")
        print("Gracias por tu compra!\n Ceba buenos mates en esa bestia!")

    def listarMates(self, tipo):
        with open('./mates/recursos/listaMates.json', 'r') as Mates:
            for Mates in Mates:
                detalles = Mates.split("|")
                if tipo == detalles[2]:
                    print(Mates)
                    return detalles
            else:
                Mate.close()
                return False
