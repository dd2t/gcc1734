from typing import Any, Callable, List
from search_problems import SearchProblem
from search_algorithms import GraphSearch
from search_algorithms.frontier_strategies import PriorityQueueFrontierStrategy


class GreedySearch(GraphSearch):
    """The Greedy algorithm is a graph traversal algorithm that just follows chosen heuristic."""

    def __init__(self, heuristic_function: Callable[[Any, SearchProblem], int]) -> None:
        self._heuristic = heuristic_function

    def run(self, problem: SearchProblem) -> List:
        """Returns a list of actions which solve the problem."""
        self._frontier = PriorityQueueFrontierStrategy(lambda node: self._heuristic(node.state, problem))
        return super().run(problem)
