# pylint: disable=W1203,C0116,R0903,C0114


from main import run_main


def test_run_main(get_args_create_section_processor, get_args_help_processor, http_url):
    """logical seq"""
    run_main(get_args_create_section_processor + [http_url])
    run_main(get_args_help_processor)
