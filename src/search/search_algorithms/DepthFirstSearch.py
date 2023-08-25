from search_algorithms import GraphSearch
from search_algorithms.frontier_strategies import StackFrontierStrategy


class DepthFirstSearch(GraphSearch):
    """A graph traversal algorithm that starts from a source node and explores
    as deeply as possible along each branch before backtracking."""

    def __init__(self) -> None:
        super().__init__(StackFrontierStrategy())
