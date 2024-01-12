import json

class Setup:
    def __init__(self, caricoAA, caricoAP, campA, campP, convA, convP, pressF, barraAA, barraAP):
        self.caricoAA = caricoAA
        self.caricoAP = caricoAP
        self.campA = campA
        self.campP = campP
        self.convA = convA
        self.convP = convP
        self.pressF = pressF
        self.barraAA = barraAA
        self.barraAP = barraAP

    def __str__(self):
        return ("{\"caricoAA\":"+str(self.caricoAA)+",\"caricoAP\":"+str(self.caricoAP)+",\"campA\":"+str(self.campA)+",\"campP\":"+str(self.campP)+",\"convA\":"+str(self.convA)+",\"convP\":"+str(self.convP)+",\"pressF\":"+str(self.pressF)+",\"barraAA\":"+str(self.barraAA)+",\"barraAP\":"+str(self.barraAP))+"}"

    def __eq__(self, other):
        if not isinstance(other, Setup):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.caricoAA == other.caricoAA and self.caricoAP == other.caricoAP and self.campA == self.campA and self.convA == self.convA and self.pressF == other.pressF and self.barraAA == other.barraAA and self.barraAP==other.barraAA

    def listMode(self):
        return "["+self.caricoAA+","+self.caricoAP+","+self.campA+","+self.campP+","+self.convA+","+self.convP+","+self.pressF+","+self.barraAA+","+self.barraAP+"]"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)