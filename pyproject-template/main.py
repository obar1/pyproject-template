"""Main Module:
Main
"""
# pylint: disable=W0703

import logging
import sys
import traceback
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
    except Exception as ex:
        logging.error(ex)
        traceback.print_exc()
