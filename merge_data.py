import os
from data_tool import DataTool
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--data-in", type=str, default="./data", help="Directory containing the input data")
parser.add_argument("--output-file", type=str, default="merged_data.json", help="Output file for the merged data")

args = parser.parse_args()
data_in_dir = args.data_in
output_file = args.output_file

data_tool = DataTool()
data_tool.merge(data_in_dir)
data_tool.write(output_file)
