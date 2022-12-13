from __future__ import annotations
from dataclasses import dataclass, field
from random import sample
from typing import Self

from BA.Bee import Bee


@dataclass
class Node:
    id: int
    connections: set[Self] = field(default_factory=set)

    def __hash__(self):
        return hash(self.id)

    def is_connected_to(self, other: Node) -> bool:
        return self in other.connections

    def connect(self, other: Node) -> None:
        if other not in self.connections:
            self.connections.add(other)
        if self not in self.connections:
            other.connections.add(self)


class UndirectedGraph(Bee, list[Node]):

    @classmethod
    def generate_random(cls, nodes_count: int, nodes_degree_range: tuple[int, int]) -> Self:
        average_node_degree = sum(nodes_degree_range) / 2
        average_edges_count = nodes_count * average_node_degree
        result = UndirectedGraph([Node(i) for i in range(nodes_count)])
        i = 0
        while i < average_edges_count / 2:
            node1, node2 = sample(result, k=2)
            if not node1.is_connected_to(node2):
                node1.connect(node2)
                i += 1
        return result

    def append(self, node: Node) -> None:
        super().append(node)
        for connected_node in node.connections:
            connected_node.connections.add(node)

    def is_clique(self) -> bool:
        for node in self:
            if len(node.connections) < len(self) - 1:
                return False
        return True

    @property
    def fitness(self) -> float:
        return len(self) * self.is_clique()
