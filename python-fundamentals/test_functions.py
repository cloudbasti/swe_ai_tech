import pytest
from functions import calculate_average, calculate_average_with_loop

def test_calculate_average():
    # Test with integers
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    # Test with floats
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5
    # Test with single value
    assert calculate_average([42]) == 42.0

def test_calculate_average_with_loop():
    # Test with integers
    assert calculate_average_with_loop([1, 2, 3, 4, 5]) == 3.0
    # Test with floats
    assert calculate_average_with_loop([1.5, 2.5, 3.5]) == 2.5
    # Test with single value
    assert calculate_average_with_loop([42]) == 42.0

def test_both_functions_give_same_result():
    test_cases = [
        [1, 2, 3, 4, 5],
        [1.5, 2.5, 3.5],
        [42],
    ]
    for numbers in test_cases:
        assert calculate_average(numbers) == calculate_average_with_loop(numbers) 