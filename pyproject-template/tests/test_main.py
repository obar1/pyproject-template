"""Unit tests."""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from main import run_main


def test_run_main(
    get_args_create_section_processor,
    get_args_help_processor,
):
    """logical seq"""
    run_main(get_args_create_section_processor + ["http://google.com/docs"])
    run_main(get_args_create_section_processor + ["https://cloud.google.com/docs"])
    run_main(get_args_help_processor)
