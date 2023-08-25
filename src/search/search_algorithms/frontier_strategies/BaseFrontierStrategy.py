from abc import ABC, abstractmethod
from typing import List
from node import Node


class BaseFrontierStrategy(ABC):
    """Base class for frontier strategies."""

    def __init__(self) -> None:
        self._frontier: List[Node] = []

    @abstractmethod
    def push(self, item: Node, *args, **kwargs) -> None:
        """Inserts an item into the frontier."""
        raise NotImplementedError

    @abstractmethod
    def pop(self) -> Node:
        """Removes an item from the frontier."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Returns True if the frontier is empty. Otherwise, returns false."""
        return len(self._frontier) == 0
    
    def clear(self) -> None:
        """Removes all items from the frontier."""
        self._frontier = []
