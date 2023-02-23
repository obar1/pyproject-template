import pytest

from lib.exceptions.some_exception import SomeException
from lib.factories.factory_provider import FactoryProvider
from lib.factories.a_factory import AFactory
from lib.tests.mocke.persist_fs import PersistFS as persist_fs

# pylint: disable=W0613


@pytest.fixture
def get_factory_provider(mock_settings_env_vars):
    return FactoryProvider(persist_fs)


def test_provide__pass(get_factory_provider):
    actual = get_factory_provider.provide()
    assert isinstance(actual, AFactory)


@pytest.fixture
def get_unsupported_factory_provider(mock_unsupported_map_yaml_env_vars):
    return FactoryProvider(persist_fs)


def test_provide__unsupported(get_unsupported_factory_provider):
    with pytest.raises(SomeException):
        get_unsupported_factory_provider.provide()
