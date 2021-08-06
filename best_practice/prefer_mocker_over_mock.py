"""
Why?
- Eliminates the chance of flaky tests due to leaks in the mocks.
  which is when a test does not reset a patch

- Less boilerplate and works better with parameterized functions and features

Follow along from:
https://www.nerdwallet.com/blog/engineering/5-pytest-best-practices/
"""
import pytest

try:
    import mock # fails on python 3
except ImportError:
    from unittest import mock

def first_test_fn():
    return 42

def another_test_fn():
    return 42

class TestManualMocking(object):
    """
    This is dangerous as you can forget to call ''stop'',
    or the test could error out, both leak state across tests
    """

    @pytest.mark.xfail(strict=True, msg="We want this to fail.")
    def test_manual(self):
        patcher = mock.patch("best_practice.prefer_mocker_over_mock.first_test_fn", return_value=84)
        patcher.start()
        assert first_test_fn() == 42
        assert False
        patcher.stop()

    def test_manual_follow_up(self):
        assert first_test_fn() == 42, "Looks like there is leaked state"

class TestDecoratorMocking(object):
    """
    This is better, but:
    1. Confusing when layering pytest decorators like @pytest.mark with @mock.patch
    2. Does not work when used with fixtures
    3. Forces - mock_fn as argument even when mock is set up and never used (boilerplate)
    """

    @pytest.mark.xfail(strict=True, msg="We want this to fail")
    @mock.patch("best_practice.prefer_mocker_over_mock.another_test_fn", return_value=84)
    def test_decorator(self, mock_fn):
        assert another_test_fn() == 84
        assert False

    def test_decorator_follow_up(self):
        assert another_test_fn() == 42

    @pytest.fixture
    @mock.patch("best_practice.prefer_mocker_over_mock.another_test_fn", return_value = 84)
    def mock_fn(self, _):
        return

    def test_decorator_with_fixture(self, mock_fn):
        assert another_test_fn() == 84, "@mock and fixtures don't mix"

class TestMockerFixture(object):
    """
    This is best, the mocker fixture reduces boilerplate and stays out
    of the declarative pytest syntax
    """

    @pytest.mark.xfail(strict=True, msg="We want this to fail.")
    def test_mocker(self, mocker):
        mocker.patch("best_practice.prefer_mocker_over_mock.another_test_fn", return_value=84)
        assert another_test_fn() == 84
        assert False

    def test_mocker_follow_up(self):
        assert another_test_fn() == 42

    @pytest.fixture
    def mock_fn(self, mocker):
        return mocker.patch("best_practice.prefer_mocker_over_mock.another_test_fn", return_value =84)

    def test_mocker_with_fixture(self, mock_fn):
        assert another_test_fn() == 84
