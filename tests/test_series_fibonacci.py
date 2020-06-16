from math_series.series import fibonacci


def test_fibonacci_basecase_0() :
    expected = 0
    actual = fibonacci(0)
    assert expected == actual


def test_fibonacci_basecase_1() :
    expected = 1
    actual = fibonacci(1)
    assert expected == actual


def test_fibonacci_5() :
    expected = 5
    actual = fibonacci(5)
    assert expected == actual


def test_fibonacci_10() :
    expected = 55
    actual = fibonacci(10)
    assert expected == actual


def test_fibonacci_50() :
    expected = 12586269025 
    actual = fibonacci(50)
    assert expected == actual



def test_fibonacci_100() :
    expected = 354224848179261915075
    actual = fibonacci(100)
    assert expected == actual
