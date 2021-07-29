def pytest_addoption(parser):
    parser.addoption("--all", action="store_true",
                     help="run all combinations")

def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))

"""
Run two tests if you do not pass --all

pytest -q test_compute.py

Will run all tests-
pytest -q all 
For this command you will also get a test failure on the last one 
"""
