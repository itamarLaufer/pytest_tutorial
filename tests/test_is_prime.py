import pytest

from pytest_tutorial import is_prime

# hard coded multi tests


def test_2_is_prime():
    assert is_prime(2)


def test_3_is_prime():
    assert is_prime(3)


def test_43_is_prime():
    assert is_prime(43)


def test_1_is_not_prime():
    assert not is_prime(1)


def test_4_is_not_prime():
    assert not is_prime(4)


def test_100_is_not_prime():
    assert not is_prime(100)


# Using parametrize phase 1


@pytest.mark.parametrize("number", (2, 3, 43))
def test_is_prime(number):
    assert is_prime(number)


@pytest.mark.parametrize("number", (1, 4, 100))
def test_is_not_prime(number):
    assert not is_prime(number)


# Using parametrize phase 2


@pytest.mark.parametrize("number, expected_result", ((2, True), (3, True), (43, True), (1, False), (4, False), (100, False)))
def test_is_prime(number, expected_result):
    assert is_prime(number) == expected_result
