import os
import yaml

class ReadYamlFile:
    def __init__(self, file: str, directory : str) -> None:
        self.file :str = file
        self.directory : str = directory

    def validate_path(self) -> bool:
        return os.path.isdir(os.environ.get('userprofile')+f"\Desktop\Configs\{self.directory}") and \
            os.path.isfile(os.environ.get('userprofile')+f"\Desktop\Configs\{self.directory}\{self.file}.yml")

    def read(self) -> list[dict]:
        try:
            if self.validate_path():
                path : str = os.environ.get('userprofile')+f"\Desktop\Configs\{self.directory}\{self.file}.yml"
                with open(path, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    if data is not None:
                        return data
                    return []
            else:
                return []
        except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
            return []
