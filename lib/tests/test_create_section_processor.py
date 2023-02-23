from lib.factories.a_factory import AFactory
from lib.processors.create_section_processor import CreateSectionProcessor
from lib.tests.mocke.persist_fs import PersistFS as persist_fs


def test_process(get_config_map, get_args_create_section_processor, http_url):
    actual: CreateSectionProcessor = AFactory(get_config_map, persist_fs).get_processor(
        get_args_create_section_processor + [http_url]
    )
    actual.process()
