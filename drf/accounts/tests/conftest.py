import pytest

from account.factories import UserFactory


@pytest.fixture
def user(db):
    return UserFactory()


@pytest.fixture
def users(db):
    return UserFactory.create_batch(5)
