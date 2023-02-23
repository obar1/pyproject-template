import pytest

from exceptions.some_exception import SomeException
from factories.factory_provider import FactoryProvider
from factories.a_factory import AFactory
from tests.mocke.persist_fs import PersistFS as persist_fs


@pytest.fixture
def get_factory_provider():
    return FactoryProvider(persist_fs)


def test_provide__pass():
    actual = get_factory_provider.provide()
    assert isinstance(actual, AFactory)


@pytest.fixture
def get_unsupported_factory_provider():
    return FactoryProvider(persist_fs)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(SomeException):
        get_unsupported_factory_provider.provide()
