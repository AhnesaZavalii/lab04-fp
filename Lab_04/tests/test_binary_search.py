from algorithms import binary_search_iter, binary_search_recursive

def test_binary_search_found() -> None:
    seq = (1, 3, 5, 7, 9, 11, 13)
    assert binary_search_recursive(seq, 7) == 3
    assert binary_search_iter(seq, 7) == 3

def test_binary_search_boundaries() -> None:
    seq = (10, 20, 30, 40, 50)
    assert binary_search_recursive(seq, 10) == 0
    assert binary_search_iter(seq, 10) == 0
    assert binary_search_recursive(seq, 50) == 4
    assert binary_search_iter(seq, 50) == 4

def test_binary_search_not_found() -> None:
    seq = (2, 4, 6, 8, 10)
    for missing in (0, 5, 12):
        assert binary_search_recursive(seq, missing) is None
        assert binary_search_iter(seq, missing) is None

def test_binary_search_empty_and_single() -> None:
    assert binary_search_recursive((), 1) is None
    assert binary_search_iter((), 1) is None
    assert binary_search_recursive((42,), 42) == 0
    assert binary_search_iter((42,), 42) == 0
    assert binary_search_recursive((42,), 7) is None
    assert binary_search_iter((42,), 7) is None

def test_binary_search_parity() -> None:
    seq = tuple(range(-50, 50, 3))
    for target in range(-60, 60):
        assert binary_search_recursive(seq, target) == binary_search_iter(seq, target)