import pytest
from sort_algorithms import Sort



def test_merge_sort():
    arr = [1,2,5,6,4,3,5,2,4]
    assert Sort.merge_sort(arr) == [1, 2, 2, 3, 4, 4, 5, 5, 6]


def test_all():
    test_merge_sort()

test_all()