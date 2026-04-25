from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      data_source: str
      zip_file: Path
      unzip_file: Path