from typing import Optional, TypeVar
from search_problems import SearchProblem

T = TypeVar('T', bound='Node')


class Node:
    """Representation of a node in the search tree."""

    def __init__(self, state, action: Optional[T], cost: int,
                 parent: Optional['Node']) -> None:
        self._state = state
        self.action = action
        self.parent_node = parent
        self.path_cost: int = parent.path_cost + cost

    def getActionSequence(self):
        actions = []

        node = self
        while node.path_cost > 0:
            actions.insert(0, node.action)
            node = node.parent_node

        return actions

    @staticmethod
    def getStartNode(problem: SearchProblem):
        return Node(state=problem.getStartState(),
                    action=None,
                    cost=0,
                    parent=None)

    def getChildNode(self, next_state, used_action: T, action_cost: int):
        return Node(state=next_state,
                    action=used_action,
                    cost=action_cost,
                    parent=self)
