from typing import List
from node import Node
from search_problems import SearchProblem
from search_algorithms import GraphSearch
from search_algorithms.frontier_strategies import StackFrontierStrategy


class IteractiveDeepeningSearch(GraphSearch):
    def __init__(self) -> None:
        super().__init__(StackFrontierStrategy())

    def run(self, problem: SearchProblem) -> List:
        """Returns a list of actions which solve the problem."""

        iteration_limit = 0
        while True:
            self._frontier.push(Node.getStartNode(problem))
            explored = set()
            print(iteration_limit)
            while not self._frontier.is_empty():
                node = self._frontier.pop()

                if node.state in explored:
                    continue

                explored.add(node.state)

                if problem.isGoalState(node.state):
                    self._frontier.clear()
                    return node.getActionSequence()
                
                if len(node.getActionSequence()) > iteration_limit:
                    self._frontier.clear()
                    continue

                for sucessor in problem.expand(node.state):
                    child_node = node.getChildNode(*sucessor)
                    self._frontier.push(child_node)
            
            iteration_limit += 1
