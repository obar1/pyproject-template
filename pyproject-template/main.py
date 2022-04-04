"""MAIN:
main
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

import logging
import sys
from typing import List

from factories.factory_provider import FactoryProvider
from factories.a_factory import AFactory
from repository.persist_fs import PersistFS as persist_fs


def run_main(argv: List[str]):
    """run main new_section"""
    factory: AFactory = FactoryProvider(persist_fs).provide()
    return factory.get_processor(argv).process()


if __name__ == "__main__":
    try:
        run_main(sys.argv)
    except AssertionError as ex:
        logging.error(ex)
