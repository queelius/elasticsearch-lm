from argparse import ArgumentParser
from json_sampler import sample_json_objects
import json

def generate_prompt(file, sample_size = 1):
    obs = sample_json_objects(file, sample_size)
    # pretty print the obs
    prompt = "Here are some examples:\n"
    prompt += "```json\n"
    prompt += json.dumps(obs, indent=2)
    prompt += "\n```\n"
    prompt += "Please generate more synthetic data based on these examples.\n"
    prompt += "Hoewver, feel free to modify the examples as you see fit.\n"
    return prompt


# run it if we call it from the command line
if __name__ == "__main__":
    parser = ArgumentParser(description="Genrate fine-tuning instructions for Elasticsearch queries.")
    parser.add_argument("infile", type=str, help="Input file containing a JSON array.")
    parser.add_argument("--size", type=int, default=1, help="Number of objects to sample (default: 1).")
    parser.add_argument("--outfile", type=str, help="Output file to write sampled objects (optional).")

    args = parser.parse_args()

    try:
        prompt = generate_prompt(args.infile, args.size)
        if args.outfile:
            with open(args.outfile, 'w') as file:
                file.write(prompt)
            print(f"Prompt written to {args.outfile}")
        else:
            print(prompt)
    except Exception as e:
        print(f"Error: {e}")
