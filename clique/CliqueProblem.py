from functools import reduce
from random import choice

from BA.BeesAlgorithm import BeesProblem
from clique.graph import UndirectedGraph, Node


class CliqueProblem(BeesProblem):

    def __init__(self, nodes_count: int, nodes_degree_range: tuple[int, int]):
        self.graph = UndirectedGraph.generate_random(nodes_count, nodes_degree_range)

    def get_bee(self, node: Node = None) -> UndirectedGraph:
        if node is None:
            node = choice(self.graph)
        neighbor_node = choice(tuple(node.connections))
        return UndirectedGraph([node, neighbor_node])

    def get_neighbor(self, bee: UndirectedGraph) -> UndirectedGraph:
        neighbor_nodes = [set(node.connections) for node in bee]
        neighbor_nodes_mutual = reduce(lambda x, y: x & y, neighbor_nodes)
        if not neighbor_nodes_mutual:
            return bee

        random_mutual_neighbor = choice(list(neighbor_nodes_mutual))
        bee.append(random_mutual_neighbor)
        return bee
