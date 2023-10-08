import os
import sys

current_dir = os.path.dirname(__file__)
src_dir = "../src"
sys.path.insert(0, os.path.abspath(os.path.join(current_dir, src_dir)))
TEST_DIR = os.path.dirname(os.path.realpath(__file__))

base_path = f'{os.getcwd()}/../src/chatregex/books'
a_study_in_scarlet_path = f'{base_path}/a_study_in_scarlet.txt'
the_secret_adversary_path = f'{base_path}/the_secret_adversary.txt'
the_sign_of_four_path = f'{base_path}/the_sign_of_four.txt'

def read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()
