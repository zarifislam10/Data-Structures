class Pair:
    """
    This class stores the destination node and the weight which are used for
    the adjacency list of a directed graph.
    If the graph is undirected, default to weight one.
    """
    def __init__(self, dest, w=1):
        self.destination = dest
        self.edge_weight = w 