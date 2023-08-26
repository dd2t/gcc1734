import heapq
from typing import Callable
from node import Node
from search_algorithms.frontier_strategies import BaseFrontierStrategy


class PriorityQueueFrontierStrategy(BaseFrontierStrategy):
    """A frontier which uses a priority FIFO based on a given function."""

    def __init__(self, priority_function: Callable[[Node], int]) -> None:
        self._frontier = []
        self._count = 0
        self._priority_function = priority_function

    def push(self, item: Node, *args, **kwargs):
        """Inserts an item into the frontier."""
        priority = self._priority_function(item)
        entry = (priority, self._count, item)
        heapq.heappush(self._frontier, entry)
        self._count += 1

    def pop(self):
        """Removes an item from the frontier."""
        (_, _, item) = heapq.heappop(self._frontier)
        return item
