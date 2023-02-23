#!/usr/bin/env python

"""Main Module:
Main
"""

import logging
import sys
import traceback
from types import NoneType
from typing import List
from lib.exceptions.some_exception import SomeException

from lib.factories.a_factory import AFactory
from lib.factories.factory_provider import FactoryProvider
from lib.repository.persist_fs import PersistFS


def run_main(argv: List[str]):
    """run main new_section"""
    factory: AFactory = FactoryProvider(PersistFS).provide()
    return factory.get_processor(argv).process()


if __name__ == "__main__":
    try:
        run_main(sys.argv)
    except AssertionError as ex:
        logging.error(ex)
    except AttributeError as ex:
        logging.error(ex)
    except Exception as ex:
        logging.error(ex)
