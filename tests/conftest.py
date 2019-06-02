import pytest
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import server
import fake_storage


@pytest.fixture
def app():
    return server.Server(fake_storage.MemoryRecordStorage(), True).get_app()
