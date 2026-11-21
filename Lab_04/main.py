"""Точка входу лабораторної роботи №4, варіант 4."""

from __future__ import annotations

import sys
import time

from algorithms import (
    Node,
    bfs_level_order,
    binary_search_iter,
    binary_search_recursive,
    dfs_preorder_iter,
    fib,
    fib_iter,
    inorder,
    postorder,
    preorder,
    quicksort,
)


def benchmark_binary_search() -> None:
    """Порівняння часу рекурсивного та ітеративного бінарного пошуку."""
    data = tuple(range(0, 1_000_000, 2))
    targets = [0, 250_000, 999_998, 123_455, -1, 1_000_000] * 5_000

    t0 = time.perf_counter()
    for target in targets:
        binary_search_recursive(data, target)
    rec_time = time.perf_counter() - t0

    t0 = time.perf_counter()
    for target in targets:
        binary_search_iter(data, target)
    iter_time = time.perf_counter() - t0

    print("Variant 4 - Binary Search Benchmark (30,000 queries on 500,000 items):")
    print(f"  Recursive: {rec_time:.4f} s")
    print(f"  Iterative: {iter_time:.4f} s")


def run() -> None:
    """Запуск демонстрації базової частини та індивідуального варіанта 4."""
    print(f"CPython recursion limit: {sys.getrecursionlimit()}\n")

    sample = [5, 1, 4, 2, 8, 2]
    print(f"QuickSort: {sample} -> {quicksort(sample)}\n")

    tree = Node(4, Node(2, Node(1), Node(3)), Node(6, None, Node(7)))
    print("Tree traversals:")
    print(f"  Preorder (recursive):  {list(preorder(tree))}")
    print(f"  Inorder (recursive):   {list(inorder(tree))}")
    print(f"  Postorder (recursive): {list(postorder(tree))}")
    print(f"  BFS (iterative):       {bfs_level_order(tree)}")
    print(f"  DFS (iterative):       {dfs_preorder_iter(tree)}\n")

    fib.cache_clear()
    print(f"Fibonacci(30): memo={fib(30)}, iter={fib_iter(30)}")
    print(f"Cache info: {fib.cache_info()}\n")

    seq = (1, 3, 5, 7, 9, 11, 13)
    print(f"Search 7 in {seq}: rec={binary_search_recursive(seq, 7)}, iter={binary_search_iter(seq, 7)}")
    print(f"Search 6 in {seq}: rec={binary_search_recursive(seq, 6)}, iter={binary_search_iter(seq, 6)}\n")
    benchmark_binary_search()


def main() -> None:
    """Точка входу програми."""
    run()


if __name__ == "__main__":
    main()
