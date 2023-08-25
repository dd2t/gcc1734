from search_algorithms import GraphSearch
from search_algorithms.frontier_strategies import QueueFrontierStrategy


class BreadthFirstSearch(GraphSearch):
    """A graph traversal algorithm that starts from a source node and explores
      all its neighbors before moving to the next level of nodes."""

    def __init__(self) -> None:
        super().__init__(QueueFrontierStrategy())
