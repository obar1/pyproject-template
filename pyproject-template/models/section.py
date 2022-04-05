"""Section:
new_section on disk
"""
# pylint: disable=W1203,C0116,R0903,C0114

from configs.config import ConfigMap


class Section:
    """Section."""

    def __init__(self, config_map: ConfigMap, http_url: str, persist_fs):
        """
        Init
        Args:
            http_url: https://cloud.google.com/docs
        """
        self.config_map = config_map
        self.http_url = http_url
        self.dir_name = self.__from_dir_to_http_url(http_url)
        self.persist_fs = persist_fs
        self.dir_readme_md = self.dir_name + "/readme.md"

    def __repr__(self):
        """repr"""
        return f"Section {self.http_url}, {self.dir_name}"

    @property
    def get_http_url(self):
        return self.http_url

    @property
    def get_dir_name(self):
        return self.dir_name

    @classmethod
    def __from_dir_to_http_url(cls, http_url):
        return http_url.replace("/", "§")

    @classmethod
    def from_http_url_to_dir(cls, dir_):
        return dir_.replace("§", "/")

    @classmethod
    def build_from_http(cls, config_map, http_url, persist_fs):
        return Section(config_map, http_url, persist_fs)

    @classmethod
    def build_from_dir(cls, config_map, persist_fs, dir_name):
        return Section(config_map, cls.from_http_url_to_dir(dir_name), persist_fs)

    def write(self):
        return self.persist_fs.make_dirs(
            self.config_map.get_repo_path + "/" + self.dir_name
        )
