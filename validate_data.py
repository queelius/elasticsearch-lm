import sys
from glob import glob
import os
from data_tool import DataTool
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("input", type=str, help="Directory of JSON files or single JSON file containing the input data")

args = parser.parse_args()
data_in = args.input

data_tool = DataTool()
valid = True
if os.path.isdir(data_in):
    # load each file separately and then validate
    for file_path in glob(os.path.join(data_in, '*.json')):
        data_tool.read(file_path)
        entry_valid = data_tool.validate()
        valid = valid and entry_valid
else:
    data_tool.read(data_in)
    valid = data_tool.validate()

print("All entries are valid." if valid else "Some entries are invalid.")