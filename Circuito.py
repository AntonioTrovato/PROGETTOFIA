class Circuito:
    def __init__(self, lunghezza, numCurve, numRettilinei,
                 numGiri, meteo, umidita):
        self.lunghezza = lunghezza
        self.numCurve = numCurve
        self.numRettilinei = numRettilinei
        self.numGiri = numGiri
        self.meteo = meteo
        self.umidita = umidita

    def __str__(self):
        return "Circuito: [lunghezza = " + str(self.lunghezza) + ", numCurve = " + str(self.numCurve) + ", numRettilinei = " + str(self.numRettilinei) + ", numGiri = " + str(self.numGiri) + ",meteo = " + str(self.meteo) + ", umidita = " + str(self.umidita) + "]"

    def getParameters(self):
        return [self.lunghezza, self.numCurve, self.numRettilinei, self.numGiri, self.meteo, self.umidita]