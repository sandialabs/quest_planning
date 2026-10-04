from pathlib import Path
from ruamel.yaml import YAML
from typing import Any
import yaml
import logging
import sys
import shutil
import os
import sys

def get_path() -> Path: 
    return Path(__file__).resolve().parent

def data_path() -> Path:
    return get_path() / "data_explan"

BASE_DIR = get_path()
DATA_DIR = data_path()
#
# def load_config() -> dict[str, Any]:
#     config_path = get_path() / config "input.yaml"
#
#     with open(config_path, encoding="utf-8") as f:
#         return yaml.safe_load(f) or {}

# def get_path():
#     """
#     Determines the base path of the application.

#     If the application is running in a frozen state (e.g., packaged with PyInstaller),
#     it returns the directory containing the executable. Otherwise, it returns the
#     directory containing the current script.

#     :return: The base path of the application.
#     :rtype: str
#     """
#     if getattr(sys, 'frozen', False):
#         exe_path = os.path.dirname(sys.executable)
#         base_path = os.path.join(exe_path, 'lib', 'quest_planning')
#     else:
#         base_path = os.path.dirname(os.path.abspath(__file__))

#     return base_path