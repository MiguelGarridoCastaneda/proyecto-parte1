from numpy import save
from algorithms import *

if __name__ == "__main__":
    # ##################################
    # g = gridGraph(23)
    # saveGraph(g)
    ##################################
    # g = erdosRenyiGraph(500, 2500)
    # saveGraph(g)
    # ##################################
    # g = gilbertGraph(500, p=0.6)
    # saveGraph(g)
    ##################################
    g = geographicGraph(30, r=0.5)
    saveGraph(g)
    ##################################
    # g = barasiAlbertGraph(30, 4)
    # saveGraph(g)
    # print(g.getEdges())
    ##################################
    # g = dorogovtsevMendesGraph(500)
    # saveGraph(g)
