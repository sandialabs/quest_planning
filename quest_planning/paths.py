from pathlib import Path
from ruamel.yaml import YAML
from typing import Any
import yaml
import logging
import sys
import shutil

def get_path() -> Path: 
    return Path(__file__).resolve().parent

def data_path() -> Path:
    return get_path() / "data_explan"

BASE_DIR = get_path()
DATA_DIR = data_path()
