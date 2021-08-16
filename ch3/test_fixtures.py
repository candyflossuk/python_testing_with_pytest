"""
Fixtures are functions run by pytest before, and sometimes after the actual test functions.
The code in them does what ever you want it to do. You can use them
to get a data set for the tests to work on. Or get a system into a known state before
running a test. Fixtures are also used to get ready for multiple tests.
"""
import pytest

@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42

"""
The @pytest.fixture() decorator is used to tell pytest that a function is a fixture.
WHen you include the fixture name in the parameter list of a test function, pytests
knows to run it before running the test. Fixtures can do work, and return data to the test function.

pytest will look for fixture names within the module OR conftest.py

- Do not import conftest.py from anywhere.
"""
