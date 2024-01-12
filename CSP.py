from Setup import Setup
import random

"""
Dati CSP:
X = {caricoAA, caricoAP, campA, campP, convA, convP, pressF, barraAA, barraAP}
D(caricoAA) = D(caricoAP) = D(barraAA) = D(barraAP) = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
D(campA) = D(campP) = {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}
D(convA) = D(convP) = {-1, 0, -1}
D(pressF) = {0, 15, 25, 50, 75, 85, 100}
"""

attributiSetup = ["caricoAA", "caricoAP", "campA", "campP", "convA", "convP", "pressF", "barraAA", "barraAP"]
dominiSetup = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
               [-1, 0, 1], [0, 15, 25, 50, 75, 85, 100]]
assegnamentiEffettuati = []

def ricercaSetupBacktracking(circuito):
    setup1 = Setup(0,0,0,0,0,0,0,0,0)
    setup1 = setupBacktracking([], circuito, setup1)
    #print("==========================================================================================")
    setup2 = Setup(0,0,0,0,0,0,0,0,0)
    setup2 = setupBacktracking([], circuito, setup2)
    #print("==========================================================================================")
    setup3 = Setup(0,0,0,0,0,0,0,0,0)
    setup3 = setupBacktracking([], circuito, setup3)
    #print("==========================================================================================")
    setup4 = Setup(0,0,0,0,0,0,0,0,0)
    setup4 = setupBacktracking([], circuito, setup4)
    #print("==========================================================================================")
    setup5 = Setup(0,0,0,0,0,0,0,0,0)
    setup5 = setupBacktracking([], circuito, setup5)
    #print("==========================================================================================")
    #print(setup1)
    #print(setup2)
    #print(setup3)
    #print(setup4)
    #print(setup5)
    return (setup1,setup2,setup3,setup4,setup5)

def setupBacktracking(assegnamento, circuito, setup):
    if(len(assegnamento) == 9):
        #se abbiamo già creato un Setup con gli stessi valori non va bene
        for setupCreato in assegnamentiEffettuati:
            if(setupCreato==setup):
                print("SetupCreato: " + str(setupCreato) + "SetupNuovo: " + str(setup))
                return None
        assegnamentiEffettuati.append(setup)
        return setup
    attrName = variabileDaAssegnareSetup(attributiSetup.copy())
    for contatore in range(len(dominioAttributoSetup(attrName))):
        attrValue = valoreDaAssegnareSetup(attrName, circuito)
        setup.__setattr__(attrName, attrValue)
        #print("Name: " + attrName + "; Value: " + str(attrValue) + "; Attr: " + str(setup.__getattribute__(attrName)) + "\n")
        #fino a che assegnamento siamo arrivati
        assegnamento.append(attrValue)
        result = setupBacktracking(assegnamento, circuito, setup)
        if(result!=None):
            return result
    return None


def variabileDaAssegnareSetup(attributi):
    return attributi.pop(random.randrange(0, 9))

def dominioAttributoSetup(attrName):
    if ((attrName == "caricoAA") or (attrName == "caricoAP") or (attrName == "barraAA") or (attrName == "barraAP")):
        return dominiSetup[0]
    if (attrName == "pressF"):
        return dominiSetup[3]
    if ((attrName == "convA") or (attrName == "convP")):
        return dominiSetup[2]
    if ((attrName == "campA") or (attrName == "campP")):
        return dominiSetup[1]

def valoreDaAssegnareSetup(attrName, circuto):
    if((circuto==1) or (circuto==2) or (circuto==9) or (circuto==10)):
        """
        C = {caricoAA = {5,6,7,8,9,10}, caricoAP={5,6,7,8,9,10},
        pressF={0,15,25,50}, barraAA={0,1,2,3,4,5}, barraAP={0,1,2,3,4,5},
        convA={-1,0}, convP={-1,0}, campA={-5,-4,-3,-2,-1,0},
        campP={-5,-4,-3,-2,-1,0}}
        """
        if((attrName=="caricoAA") or (attrName=="caricoAP")):
            return dominiSetup[0][random.randrange(4, 9)]
        if(attrName=="pressF"):
            return dominiSetup[3][random.randrange(0, 4)]
        if((attrName=="barraAA") or (attrName=="barraAP")):
            return dominiSetup[0][random.randrange(0, 5)]
        if((attrName=="convA") or (attrName=="convP")):
            return dominiSetup[2][random.randrange(0, 2)]
        if((attrName=="campA") or (attrName=="campP")):
            return dominiSetup[1][random.randrange(0, 6)]
    if((circuto==4) or (circuto==5)):
        """
        C = {caricoAA = {5,6,7,8,9,10}, caricoAP={5,6,7,8,9,10},
        pressF={50,75,85,100}, barraAA={0,1,2,3,4,5}, barraAP={0,1,2,3,4,5},
        convA={0,1}, convP={0,1}, campA={0,1,2,3,4,5},
        campP={0,1,2,3,4,5}}
        """
        if((attrName=="caricoAA") or (attrName=="caricoAP")):
            return dominiSetup[0][random.randrange(4, 9)]
        if (attrName == "pressF"):
            return dominiSetup[3][random.randrange(3, 7)]
        if((attrName=="campA") or (attrName=="campP")):
            return dominiSetup[1][random.randrange(5, 11)]
        if((attrName=="barraAA") or (attrName=="barraAP")):
            return dominiSetup[0][random.randrange(0, 5)]
        if((attrName=="convA") or (attrName=="convP")):
            return dominiSetup[2][random.randrange(0, 2)]
    if((circuto==5) or (circuto==6) or (circuto==11) or (circuto==12)):
        """
        C = {caricoAA = {0,1,2,3,4,5}, caricoAP={0,1,2,3,4,5},
        pressF={0,15,25,50}, barraAA={5,6,7,8,9,10}, barraAP={5,6,7,8,9,10},
        convA={0,1}, convP={0,1}, campA={0,1,2,3,4,5},
        campP={0,1,2,3,4,5}}
        """
        if((attrName=="caricoAA") or (attrName=="caricoAP")):
            return dominiSetup[0][random.randrange(0, 5)]
        if (attrName == "pressF"):
            return dominiSetup[3][random.randrange(0, 4)]
        if((attrName=="campA") or (attrName=="campP")):
            return dominiSetup[1][random.randrange(0, 6)]
        if((attrName=="barraAA") or (attrName=="barraAP")):
            return dominiSetup[0][random.randrange(4, 9)]
        if((attrName=="convA") or (attrName=="convP")):
            return dominiSetup[2][random.randrange(1, 3)]
    if((circuto==7) or (circuto==8)):
        """
        C = {caricoAA = {0,1,2,3,4,5}, caricoAP={0,1,2,3,4,5},
        pressF={50,75,85,100}, barraAA={5,6,7,8,9,10}, barraAP={5,6,7,8,9,10},
        convA={0,1}, convP={0,1}, campA={0,1,2,3,4,5},
        campP={0,1,2,3,4,5}}
        """
        if((attrName=="caricoAA") or (attrName=="caricoAP")):
            return dominiSetup[0][random.randrange(0, 5)]
        if (attrName == "pressF"):
            return dominiSetup[3][random.randrange(3, 7)]
        if((attrName=="campA") or (attrName=="campP")):
            return dominiSetup[1][random.randrange(0, 6)]
        if((attrName=="barraAA") or (attrName=="barraAP")):
            return dominiSetup[0][random.randrange(4, 9)]
        if((attrName=="convA") or (attrName=="convP")):
            return dominiSetup[2][random.randrange(1, 3)]

#ricercaSetupBacktracking(1)