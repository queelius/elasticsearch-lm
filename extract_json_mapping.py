import os
import json
from data_tool import DataTool
from extract_json import extract_json
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("file", type=str, help="The file to extract JSON objects from.")
parser.add_argument("--out", type=str, default=None, help="The output JSON file.")

args = parser.parse_args()
filename = args.file

# make sure not to overwrite existing files
output_file = args.out
if output_file is None:
    output_file = f"{filename}.json"

i = 1
while os.path.exists(output_file):
    output_file = f"{filename}_{i}.json"
    i += 1

data_tool = DataTool()
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
    objs = extract_json(text)
    mappings = []
    for obj in objs:
        valid = data_tool.validate_entry(obj)
        if valid:
            mappings.append(obj)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(mappings, outfile, ensure_ascii=False, indent=2)