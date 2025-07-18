from graph import Graph
from graph_node import GraphNode

def main():
    n0 = GraphNode(0)
    n1 = GraphNode(1)
    n2 = GraphNode(2)
    n3 = GraphNode(3)
    n4 = GraphNode(4)
    n5 = GraphNode(5)
    n6 = GraphNode(6)
    n7 = GraphNode(7)
    
    g = Graph()
    g.connect(n0, n1)
    g.connect(n0, n2)
    g.connect(n1, n2)
    g.connect(n1, n3)
    g.connect(n2, n3)
    g.connect(n2, n4)
    g.connect(n3, n6)
    g.connect(n4, n5)
    g.connect(n5, n6)
    g.connect(n5, n7)
    g.connect(n6, n7)
    
    print(g.is_bipartite())

if __name__ == "__main__":
    main() 