import json
from types import SimpleNamespace

from AlberoDiDecisione import decisionTree
from CSP import ricercaSetupBacktracking
from CircuitiCampionato import mostraCircuiti

#circuito = mostraCircuiti()
from Circuito import Circuito
from Setup import Setup

f = open("C:\\Users\\anton\\git\\AM-GP-project\\src\\IA.txt", "r")
circuitoJSON = json.loads(f.read())

circuito = Circuito(circuitoJSON["lunghezza"],circuitoJSON["numCurve"],circuitoJSON["numRettilinei"],
                    circuitoJSON["numGiri"],circuitoJSON["meteo"],circuitoJSON["umidita"])

f.close()

#chiamiamo l'albero di decisione
circuitoType = decisionTree(circuito)[0]

print("\nCircuito: " + str(circuito) + "\nCircuitoType: " + str(circuitoType))

setup1, setup2, setup3, setup4, setup5 = ricercaSetupBacktracking(circuitoType)

print("\nSetup1: " + str(setup1) + "\nSetup2: " + str(setup2) + "\nSetup3: " + str(setup3) +
      "\nSetup4: " + str(setup4) + "\nSetup5: " + str(setup5))

f = open("C:\\Users\\anton\\git\\AM-GP-project\\src\\IA.txt", "w")

f.write(str(setup1)+"\n"+str(setup2)+"\n"+str(setup3)+"\n"+str(setup4)+"\n"+str(setup5))