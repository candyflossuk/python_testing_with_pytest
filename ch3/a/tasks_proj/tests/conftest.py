import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after"""
    # Setup : start_db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # where testing happens

    # Teardown : stop_db
    tasks.stop_tasks_db()
