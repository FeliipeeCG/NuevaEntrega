from mates.bombilla import Bombilla


def creaBombilla():
    newBombilla = Bombilla("Acero quirurgico", "Cordoba")
    print(newBombilla.fabricarBombilla("AQ-C", "AQ Cordobesa"))


def ComprarBombilla():
    getBombilla = Bombilla()
    print(getBombilla.obtenerBombilla("AQ-C"))


def fabricarMate():
    newMate = Mate("De madera", "250ml")
    newMate.fabricarMate("MADERA", "MD250", "AQ-C")

    fabricarMate()
