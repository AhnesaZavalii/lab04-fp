from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from random import choice
from typing import Generator, Optional, Sequence


def quicksort(xs: list[int]) -> list[int]:
    if len(xs) <= 1:
        return xs[:]
    pivot = choice(xs)
    left = [x for x in xs if x < pivot]
    mid = [x for x in xs if x == pivot]
    right = [x for x in xs if x > pivot]
    return quicksort(left) + mid + quicksort(right)


@dataclass(slots=True)
class Node:
    key: int
    left: Optional[Node] = None
    right: Optional[Node] = None


def preorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return
    yield t.key
    yield from preorder(t.left)
    yield from preorder(t.right)


def inorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return
    yield from inorder(t.left)
    yield t.key
    yield from inorder(t.right)


def postorder(t: Optional[Node]) -> Generator[int, None, None]:
    if t is None:
        return
    yield from postorder(t.left)
    yield from postorder(t.right)
    yield t.key


def bfs_level_order(t: Optional[Node]) -> list[int]:
    if t is None:
        return []
    q: deque[Node] = deque([t])
    out: list[int] = []
    while q:
        n = q.popleft()
        out.append(n.key)
        if n.left is not None:
            q.append(n.left)
        if n.right is not None:
            q.append(n.right)
    return out


def dfs_preorder_iter(t: Optional[Node]) -> list[int]:
    if t is None:
        return []
    stack: list[Node] = [t]
    out: list[int] = []
    while stack:
        n = stack.pop()
        out.append(n.key)
        if n.right is not None:
            stack.append(n.right)
        if n.left is not None:
            stack.append(n.left)
    return out


@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_iter(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def binary_search_recursive(
    seq: Sequence[int],
    target: int,
    low: int = 0,
    high: Optional[int] = None,
) -> Optional[int]:
    if high is None:
        high = len(seq) - 1
    if low > high:
        return None
    mid = (low + high) // 2
    mid_val = seq[mid]
    if mid_val == target:
        return mid
    if target < mid_val:
        return binary_search_recursive(seq, target, low, mid - 1)
    return binary_search_recursive(seq, target, mid + 1, high)


def binary_search_iter(seq: Sequence[int], target: int) -> Optional[int]:
    low = 0
    high = len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_val = seq[mid]
        if mid_val == target:
            return mid
        if target < mid_val:
            high = mid - 1
        else:
            low = mid + 1
    return None