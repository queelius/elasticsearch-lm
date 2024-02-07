import json
import random
import argparse
import os

def sample_json_objects(file_path, sample_size):
    """
    Samples a specified number of objects from a JSON array stored in a file.

    Args:
    - file_path (str): The path to the file containing the JSON array.
    - sample_size (int): The number of objects to sample.

    Returns:
    - list: A list of sampled JSON objects.
    """
    with open(file_path, 'r') as file:
        json_array = json.load(file)
    
    if sample_size > len(json_array):
        raise ValueError("Sample size cannot be greater than the number of objects in the file.")
    
    sampled_objects = random.sample(json_array, sample_size)
    return sampled_objects

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sample JSON objects from a file.")
    parser.add_argument("in_file", type=str, help="Input file containing a JSON array.")
    parser.add_argument("--sample-size", type=int, default=1, help="Number of objects to sample (default: 1).")
    parser.add_argument("--out_file", type=str, help="Output file to write sampled objects (optional).")

    args = parser.parse_args()
    if not args.out_file:
        base, ext = os.path.splitext(args.in_file)
        args.out_file = f"{base}.sample{ext}"

    try:
        sampled_objects = sample_json_objects(args.in_file, args.sample_size)
        with open(args.out_file, 'w') as file:
            json.dump(sampled_objects, file, indent=2)
        print(f"Sampled {args.sample_size} objects written to {args.out_file}")
    except Exception as e:
        print(f"Error: {e}")
