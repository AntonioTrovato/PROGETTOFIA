from DataSet import dataSetBuilder
import pandas as pd
import graphviz
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def decisionTree(circuito):
    #prendiamo il dataset e le etichette salvandole in X ed y
    X, y = dataSetBuilder()

    """
    dataFrame = pd.DataFrame(X)
    dataFrame["Category"] = y
    print(dataFrame)
    """

    #stabiliamo il dataset di test e di training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=18, random_state=42)

    #print(str(len(X_train)) + "///" + str(len(X_test)))

    #creiamo l'albero ed addestriamolo
    decision_tree = tree.DecisionTreeClassifier()
    decision_tree = decision_tree.fit(X_train, y_train)

    """
    dot_data = tree.export_graphviz(decision_tree, out_file=None)
    graph = graphviz.Source(dot_data)
    print(graph)
    """

    #effettuiamo il test
    #y_pred = decision_tree.predict(X_test)

    #print(y_pred)

    #print(accuracy_score(y_test, y_pred, normalize=True))

    """
    result = pd.DataFrame()
    result["gt"] = y_test
    result["pred"] = y_pred
    print(result)
    """

    return decision_tree.predict([[circuito.__getattribute__("lunghezza"), circuito.__getattribute__("numCurve"),
              circuito.__getattribute__("numRettilinei"), circuito.__getattribute__("numGiri"),
              circuito.__getattribute__("meteo"), circuito.__getattribute__("umidita")]])
