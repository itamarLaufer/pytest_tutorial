from pytest_tutorial import is_prime

# hard coded multi tests


def test_2_is_prime():
    assert is_prime(2)


def test_3_is_prime():
    assert is_prime(3)


def test_43_is_prime():
    assert is_prime(3)


def test_1_is_not_prime():
    assert not is_prime(1)


def test_4_is_not_prime():
    assert not is_prime(4)


def test_100_is_not_prime():
    assert not is_prime(100)
