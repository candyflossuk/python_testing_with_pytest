def test_in():
    assert 1 not in [2, 3, 4]
    assert 3 in [2, 3, 4]


def test_a_less_than_b():
    assert 'a' < 'b'


def test_fizz_in_buzz():
    assert 'fizz' not in 'fissbuzz'
    assert 'fizz' in 'fizzbuzz'
