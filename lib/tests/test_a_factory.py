import pytest

from lib.factories.a_factory import AFactory
from lib.tests.mocke.persist_fs import PersistFS as persist_fs


def test_get_processor_fail(get_config_map, get_args_soemthing_invalid):
    actual = AFactory(get_config_map, persist_fs)
    with pytest.raises(ValueError):
        actual.get_processor(get_args_soemthing_invalid)
