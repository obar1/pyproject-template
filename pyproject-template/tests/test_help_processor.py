# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613
from factories.a_factory import AFactory
from processors.help_processor import HelpProcessor, VERSION
from tests.moke.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_help_processor):
    actual: HelpProcessor = AFactory(get_config_map, persist_fs).get_processor(
        get_args_help_processor
    )
    curr_version = "0.0.0"
    assert actual.process() == f'{VERSION}"{curr_version}"'
