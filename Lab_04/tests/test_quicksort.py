import random

from algorithms import quicksort


def test_quicksort_basic() -> None:
    assert quicksort([]) == []
    assert quicksort([1]) == [1]
    assert quicksort([3, 2, 1]) == [1, 2, 3]
    assert quicksort([2, 2, 1, 3, 2]) == [1, 2, 2, 2, 3]


def test_quicksort_does_not_mutate_input() -> None:
    original = [5, 1, 4, 2, 8]
    copy_before = original[:]
    result = quicksort(original)
    assert result == [1, 2, 4, 5, 8]
    assert original == copy_before


def test_quicksort_random() -> None:
    xs = [random.randint(-1000, 1000) for _ in range(1000)]
    assert quicksort(xs) == sorted(xs)