from typing import List
from pair import Pair

class GraphNode:
    def __init__(self, d: int):
        self.data = d
        self.adj_list: List[Pair] = []
    
    def add_neighbor(self, d: 'GraphNode', w: int = 1) -> None:
        """
        Should be utilized by the Graph.connect() method when we set a as the neighbor of b
        and vice versa.
        
        If w is omitted, then the graph is not a weighted graph, default value of w is 1.
        """
        self.adj_list.append(Pair(d, w))
    
    def remove_neighbor(self, n: 'GraphNode') -> None:
        for i, pair in enumerate(self.adj_list):
            if pair.destination == n:
                self.adj_list.pop(i)
                return
    
    @property
    def data(self) -> int:
        return self._data
    
    @data.setter
    def data(self, d: int) -> None:
        self._data = d
    
    def degree(self) -> int:
        """Return the degree of the node"""
        return len(self.adj_list)
    
    def get_neighbors(self) -> List[Pair]:
        """Return the neighbor list"""
        return self.adj_list 