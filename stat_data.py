import sys
from glob import glob
import os
from data_tool import DataTool
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", type=str, help="File containing the JSON data")
args = parser.parse_args()
file = args.file

data_tool = DataTool()
if os.path.isfile(file):
    for file_path in glob(os.path.join(file)):
        data_tool.read(file_path)
        data = data_tool.stats()
else:
    print(f"File not found: {file}")
