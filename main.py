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
    # g = geographicGraph(500, r=0.7)
    # saveGraph(g)
    ##################################
    # g = barasiAlbertGraph(500, 80)
    # saveGraph(g)
    ##################################
    g = dorogovtsevMendesGraph(500)
    saveGraph(g)
