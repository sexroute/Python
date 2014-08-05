import sys
import os

tests_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..','..')

# TEST_DIR = os.path.abspath(os.path.dirname(__file__))
print tests_dir
sys.path.append(tests_dir)

