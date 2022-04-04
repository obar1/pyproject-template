# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import pytest

from configs.config import ConfigMap
from factories.a_factory import AFactory
from tests.mocke.persist_fs import PersistFS as persist_fs





def test_get_processor_fail(get_config_map, get_args_soemthing_invalid):
    actual = AFactory(get_config_map, persist_fs)
    with pytest.raises(ValueError):
        actual.get_processor(get_args_soemthing_invalid)
