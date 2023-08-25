from typing import List
from search_algorithms.frontier_strategies import BaseFrontierStrategy
from node import Node
from search_problems import SearchProblem


class GraphSearch:
    """Implementation of the graph search algorithm."""

    def __init__(self, frontier_strategy: BaseFrontierStrategy) -> None:
        self._frontier = frontier_strategy

    def run(self, problem: SearchProblem) -> List:
        """Returns a list of actions which solve the problem."""
        self._frontier.push(Node.getStartNode(problem))
        explored = set()

        while not self._frontier.is_empty():
            node = self._frontier.pop()

            if node.state in explored:
                continue

            explored.add(node.state)

            if problem.isGoalState(node.state):
                self._frontier.clear()
                return node.getActionSequence()
            
            for sucessor in problem.expand(node.state):
                child_node = node.getChildNode(*sucessor)
                self._frontier.push(child_node)

        self._frontier.clear()
        return []
