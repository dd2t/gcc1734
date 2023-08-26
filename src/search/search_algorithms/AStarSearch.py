from typing import Any, Callable, List
from search_problems import SearchProblem
from search_algorithms import GraphSearch
from search_algorithms.frontier_strategies import PriorityQueueFrontierStrategy


class AStarSearch(GraphSearch):
    """The A* search algorithm is a graph traversal algorithm that combines
    UCS algorithm with heuristics."""

    def __init__(self, heuristic_function: Callable[[Any, SearchProblem], int]) -> None:
        self._heuristic = heuristic_function

    def run(self, problem: SearchProblem) -> List:
        """Returns a list of actions which solve the problem."""
        node_total_cost_function = lambda node: node.path_cost + self._heuristic(node.state, problem)
        self._frontier = PriorityQueueFrontierStrategy(node_total_cost_function)
        return super().run(problem)
