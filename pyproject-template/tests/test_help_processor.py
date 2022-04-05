# pylint: disable=W1203,C0116,R0903,C0114
from factories.a_factory import AFactory
from processors.help_processor import HelpProcessor, VERSION
from tests.mocke.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_help_processor):
    actual: HelpProcessor = AFactory(get_config_map, persist_fs).get_processor(
        get_args_help_processor
    )
    curr_version = "0.0.0"
    assert actual.process() == f'{VERSION}"{curr_version}"'
