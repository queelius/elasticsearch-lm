from langchain.llms import Ollama
from generate_prompt import generate_prompt
import os
import requests
import json
import argparse
from generate_prompt import generate_prompt
import json

SERVER_URL = os.getenv("OLLAMA_SERVER", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_MODEL", "ollama")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic data from Ollama")
    parser.add_argument("--model", default=MODEL, help="Model to use")
    parser.add_argument("--server", default=SERVER_URL, help="Server URL. Defaults to http://localhost:11434")
    parser.add_argument("in_file", help="The JSON file containing the high quality data for synthetic data generation")
    parser.add_argument("--out_file", help="The output file to save the synthetic data")
    parser.add_argument("--num_samples", type=int, default=1, help="Number of JSON objects to generate")
    parser.add_argument("--num_examples", type=int, default=1, help="Number of examples to use for each synthetic data sample")
    parser.add_argument("--temp", type=float, default=1.5, help="Temperature for sampling")
    parser.add_argument("--top_p", type=float, default=0.95, help="Top p for sampling")
    parser.add_argument("--top_k", type=int, default=100, help="Top k for sampling")
    parser.add_argument("--max_length", type=int, default=10000, help="Maximum length of the generated text")
    args = parser.parse_args()

    for i in range(args.num_samples):

        prmpt = generate_prompt(args.in_file, args.num_examples)
        data = {
            "prompt": prmpt,
            "model": args.model,
            "format": "json",
            "stream": False,
            "options": {"temperature": args.temp, "top_p": args.top_k,
                        "top_k": args.top_k, "max_length": args.max_length }
        }

        resp = requests.post(f'{SERVER_URL}/api/generate', json=data, stream=False)
        json_data = json.loads(resp.text)
        print(json.dumps(json.loads(json_data["response"]), indent=2))