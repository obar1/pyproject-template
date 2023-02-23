#!/usr/bin/env python

"""Main Module:
Main
"""

import sys
from typing import List
from lib.factories.a_factory import AFactory
from lib.factories.factory_provider import FactoryProvider
from lib.repository.persist_fs import PersistFS


def run_main(argv: List[str]):
    """run main new_section"""
    factory: AFactory = FactoryProvider(PersistFS).provide()
    return (
        factory.get_processor(argv).process()
        if factory.get_processor(argv) is not None
        else None
    )


def demo():
    """Just a demo"""
    import os

    os.environ["CONFIG_FILE"] = "./map.yaml"
    print(run_main(sys.argv))


if __name__ == "__main__":
    demo()
