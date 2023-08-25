from node import Node
from search_algorithms.frontier_strategies import BaseFrontierStrategy


class StackFrontierStrategy(BaseFrontierStrategy):
    """A frontier with LIFO policy."""

    def push(self, item: Node, *args, **kwargs):
        """Inserts an item into the frontier."""
        self._frontier.append(item)

    def pop(self):
        """Removes an item from the frontier."""
        return self._frontier.pop()
