import pytest

from pyproject import app
from pyproject.models import metadata
from pyproject.database import engine


@pytest.fixture
def client():
    client = app.test_client()

    metadata.create_all(engine)

    yield client
