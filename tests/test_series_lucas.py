from math_series.series import lucas


def test_lucas_basecase_0() :
    expected = 2
    actual = lucas(0)
    assert expected == actual


def test_lucas_basecase_1() :
    expected = 1
    actual = lucas(1)
    assert expected == actual


def test_lucas_5() :
    expected = 11
    actual = lucas(5)
    assert expected == actual


def test_lucas_10() :
    expected = 123
    actual = lucas(10)
    assert expected == actual


def test_lucas_50() :
    expected = 28143753123 
    actual = lucas(50)
    assert expected == actual



def test_lucas_100() :
    expected = 792070839848372253127
    actual = lucas(100)
    assert expected == actual
