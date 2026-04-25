from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
      root_dir: Path
      data_source: str
      zip_file: Path
      unzip_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
      root_dir: Path
      data_path: Path
      status_file: str
      schema: dict