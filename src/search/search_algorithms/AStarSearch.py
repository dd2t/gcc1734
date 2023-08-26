from typing import Any, Callable
from search_problems import SearchProblem
from search_algorithms import GraphSearch
from search_algorithms.frontier_strategies import PriorityQueueFrontierStrategy


class AStarSearch(GraphSearch):
    """The A* search algorithm is a graph traversal algorithm that combines
    UCS algorithm with heuristics."""

    def __init__(self, problem: SearchProblem,
                 heuristic_function: Callable[
                     [Any, SearchProblem], int]) -> None:
        node_total_cost_function = lambda node: node.path_cost + heuristic_function(node.state, problem)
        super().__init__(PriorityQueueFrontierStrategy(node_total_cost_function))
