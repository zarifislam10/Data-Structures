from typing import Set, List
from collections import deque
from graph_node import GraphNode

class Graph:
    def __init__(self):
        self.graph: Set[GraphNode] = set()
    
    def connect(self, a: GraphNode, b: GraphNode, w: int = 1) -> None:
        """
        Connect nodes a and b. If graph is not weighted, 
        then the weight defaults to 1.
        """
        self.graph.add(a)
        self.graph.add(b)
        a.add_neighbor(b, w)
        b.add_neighbor(a, w)
    
    def delete(graph, node) -> None:
        if current in graph:
            # Remove node from neighbors' lists
            for neighbor in graph[current]:
                graph[neighbor].remove(current)
            # Remove the node itself
            del graph[current]

    
    def bfs(self, init_node: GraphNode) -> Set[GraphNode]:
        """
        Perform Breadth First Search on the graph.
        Print each node you visit.
        """
        queue = deque([init_node])
        visited = {init_node}
        
        while queue:
            node = queue.popleft()
            print(node.data)
            node_neighbors = node.get_neighbors()
            for pair in node_neighbors:
                neighbor = pair.destination
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return visited
    
    def dfs(self, init_node: GraphNode) -> None:
        """
        Perform Depth First Search on the graph.
        Print each node you visit.
        """
        stack = [init_node]
        visited = {init_node}
        
        while stack:
            node = stack.pop()
            print(node.data)
            node_neighbors = node.get_neighbors()
            for pair in node_neighbors:
                neighbor = pair.destination
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)
    
import heapq

    def shortest_path(self, a: GraphNode, b: GraphNode) -> None:
        """
        Given two nodes, a and b, find the shortest path if it exists.
        Shortest path is defined in terms of edge weights (aka smallest weight sum).
        """
        heap = [(0, a, [])]  # (cost, current_node, path_so_far)
        visited = set()

        while heap:
            cost, node, path = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            path = path + [node]

            if node == b:
                print(" -> ".join(str(n.value) for n in path), f"Total cost: {cost}")
                return

            for neighbor, weight in node.neighbors:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path))

      # Implementation left as an exercise

    
    def get_a_node(self) -> GraphNode:
        if not self.graph:
            return None
        return next(iter(self.graph))
    
    def is_bipartite(self) -> bool:
        """
        Can we color the graph in such a way that
        each neighbor is of alternating red/blue color?
        """
        if len(self.graph) < 2:
            return True
            
        red_nodes = set()
        blue_nodes = set()
        init_node = self.get_a_node()
        
        queue = deque([init_node])
        red_nodes.add(init_node)
        
        while queue:
            node = queue.popleft()
            node_neighbors = node.get_neighbors()
            print(node.data)
            for pair in node_neighbors:
                neighbor = pair.destination
                
                if ((node in red_nodes and neighbor in red_nodes) or
                    (node in blue_nodes and neighbor in blue_nodes)):
                    return False
                    
                if neighbor not in red_nodes and neighbor not in blue_nodes:
                    queue.append(neighbor)
                    if node in red_nodes:
                        blue_nodes.add(neighbor)
                    else:
                        red_nodes.add(neighbor)
        return True
    
    def is_connected(self) -> bool:
        """
        Are all the nodes connected to each other?
        """
        visited = set()
        for node in self.graph:
            visited = self.bfs(node)
            break
        return len(visited) == len(self.graph) 
