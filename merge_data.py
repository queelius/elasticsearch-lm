from data_tool import DataTool
from argparse import ArgumentParser
import os
import sys

def generate_output_filename(directory, base_filename, specified_filename=None):
    """
    Generates a unique output filename based on the specified conditions.
    
    Args:
    - directory (str): The directory containing the input data.
    - base_filename (str): The base name for the output file, derived from the directory name.
    - specified_filename (str): An optional specified filename. If provided, this filename is used.
    
    Returns:
    - str: A unique filename for the output file.
    """
    # Use the specified filename if provided
    if specified_filename:
        output_path = os.path.join(directory, specified_filename)
        if not os.path.exists(output_path):
            return output_path
        base_filename = os.path.splitext(specified_filename)[0]
    else:
        output_path = os.path.join(directory, f"{base_filename}.json")
        if not os.path.exists(output_path):
            return output_path
    
    # If the base filename exists, find a unique filename by appending an integer
    n = 1
    while os.path.exists(os.path.join(directory, f"{base_filename}-{n}.json")):
        n += 1
    return os.path.join(directory, f"{base_filename}-{n}.json")

parser = ArgumentParser(description="Merge JSON data from files in a directory and output to a specified file.")
parser.add_argument("--in-dir", type=str, help="Directory containing the input data files.")
parser.add_argument("--out", type=str, help="Optional output file name. If not specified, a name based on the input directory will be generated.")

args = parser.parse_args()

data_tool = DataTool()
data_tool.merge(args.in_dir)
data_tool.write(args.out)

# Notify user about the output file
print(f"Output saved to: {args.out}")
