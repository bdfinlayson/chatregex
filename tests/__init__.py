import os
import sys

current_dir = os.path.dirname(__file__)
src_dir = "../src"
sys.path.insert(0, os.path.abspath(os.path.join(current_dir, src_dir)))
TEST_DIR = os.path.dirname(os.path.realpath(__file__))


def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()