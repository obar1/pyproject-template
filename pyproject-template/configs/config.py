"""Config:

like

config:
  type: map
repo:
  path: ./repo
  sorted : true

"""


class Config:
    """Config"""

    def __init__(self, persist_fs, map_yaml_path):
        """persist_fs_load_file: f()  to load file as dict[]"""
        self.persist_fs = persist_fs
        assert self.persist_fs.load_file(map_yaml_path) is not None
        self.map_yaml_path = map_yaml_path

    def __repr__(self):
        """repr"""
        return f"map_yaml_path:{self.map_yaml_path}"

    @property
    def load(self):
        """load yaml file"""
        return self.persist_fs.load_file(self.map_yaml_path)

    @property
    def get_type(self):
        """Returns config type."""
        return self.load["type"]


class ConfigMap(Config):
    """ConfigMap specific to  actual impl"""

    def __init__(self, map_yaml_path, persist_fs):
        """init"""
        super().__init__(persist_fs, map_yaml_path)

    @property
    def get_repo_path(self):
        """T Returns path."""
        return self.load["repo"]["path"]

    @property
    def get_repo_sorted(self) -> bool:
        """T Returns sorted."""
        return bool(self.load["repo"]["sorted"])
