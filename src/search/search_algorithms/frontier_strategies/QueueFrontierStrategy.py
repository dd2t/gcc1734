from node import Node
from search_algorithms.frontier_strategies import BaseFrontierStrategy


class QueueFrontierStrategy(BaseFrontierStrategy):
    """A frontier with FIFO policy."""

    def push(self, item: Node, *args, **kwargs):
        """Inserts an item into the frontier."""
        self._frontier.insert(0, item)

    def pop(self):
        """Removes an item from the frontier."""
        return self._frontier.pop()
