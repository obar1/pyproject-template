"""FactoryProvider:
provides the actual factory based on the type value
"""


import os

from configs.config import Config, ConfigMap
from exceptions.some_exception import SomeException
from factories.a_factory import AFactory

MAP = "map"

CONFIG_FILE = "CONFIG_FILE"


class FactoryProvider:
    """FactoryProvider class.
    Provides factory implementation.
    """

    def __init__(self, persist_fs):
        self.config_file = os.getenv(CONFIG_FILE)
        if self.config_file is None:
            raise SomeException("CONFIG_FILE not set in os env")
        self.persist_fs = persist_fs

    def provide(self) -> AFactory:
        """T The method returns instance of Factory."""
        get_type = Config(self.persist_fs, self.config_file).get_type
        if get_type == MAP:
            config_map = ConfigMap(self.config_file, self.persist_fs)
            return AFactory(config_map, self.persist_fs)
        raise SomeException(f"ConfigNotImplementedError {get_type}")
