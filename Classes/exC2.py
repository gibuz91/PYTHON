#DEFINIZIONE CONCETTO DI CLASSE E SUPERCLASSE
class Poligono(object):
    def __init__(self, _numLati):
        self.numLati = _numLati
    def calcolaPerimetro(self):
        pass
    def calcolaArea(self):
        pass
    def getNumLati(self):
        return self.numLati

class Rettangolo(Poligono):
    def __init__(self, _base, _altezza):
        super(Rettangolo, self).__init__(4)
        self.base = _base
        self.altezza = _altezza

    def calcolaPerimetro(self):
        return (self.base + self.altezza) * 2

    def calcolaArea(self):
        return (self.base * self.altezza)

class Triangolo(Poligono):
    def __init__(self, _lato):
        super(Triangolo, self).__init__(3)
        self.lato = _lato

    def calcolaPerimetro(self):
        return (self.lato * 3)

    def calcolaArea(self):
        return (self.lato * self.lato) / 2

baseR = int(input("Inserire base rettangolo: "))
altezzaR = int(input("Inserire altezza rettangolo: "))
print("")

rettangolo = Rettangolo(baseR, altezzaR);

print(f"Il rettangolo ha {rettangolo.getNumLati()} lati")
print(f"Il perimetro del rettangolo è {rettangolo.calcolaPerimetro()}")
print(f"L'area del rettangolo è {rettangolo.calcolaArea()}")
print("")

lato = int(input("Inserire lato triangolo: "))
print("")

triangolo = Triangolo(lato)

print(f"Il rettangolo ha {triangolo.getNumLati()} lati")
print(f"Il perimetro del rettangolo è {triangolo.calcolaPerimetro()}")
print(f"L'area del rettangolo è {triangolo.calcolaArea()}")
