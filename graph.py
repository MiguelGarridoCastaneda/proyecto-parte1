from edge import Edge
from node import Node


class Graph:
    def __init__(self):
        self.nodes = {}  # Graph nodes
        self.edges = {}  # Graph edges
        self.typee = None  # Type of graph
        self.attr = {}

    def addNode(self, name):
        """
        Add node to graph.
        :param name: the name of the node
        """
        # First check if node already exists
        n = self.nodes.get(name)

        if n is None:
            n = Node(name)

            self.nodes[name] = n

        return n

    def addEdge(self, s, t, label):
        """
        Add edge to graph.
        :param s: source node
        :param t: target node
        :param label: s->t
        """
        e = self.edges.get(label)

        if e is None:
            n1 = self.addNode(s)
            n2 = self.addNode(t)
            e = Edge(n1, n2, label)

            self.edges[label] = e
            n1.attr["NEIGHBORS"].append(n2)
            n1.attr['EDGES'].append(e)
            n2.attr["NEIGHBORS"].append(n1)
            n2.attr['EDGES'].append(e)

        return e

    def getNodes(self):
        """
        Return list of nodes
        """
        total_nodes = list(self.nodes.keys())
        return total_nodes

    def getEdges(self):
        """
        Return list of edges
        """
        total_edges = [[edge.s.id, edge.t.id] for edge in self.edges.values()]
        return total_edges
