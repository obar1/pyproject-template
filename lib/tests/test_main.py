import pytest
from lib.run_from_cli import run_main


@pytest.mark.skip(reason="no way of currently testing this")
def test_run_main(get_args_create_section_processor, get_args_help_processor, http_url):
    """logical seq"""
    run_main(get_args_create_section_processor + [http_url])
    run_main(get_args_help_processor)
