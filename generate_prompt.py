from json_sampler import sample_json_objects
import json

def generate_prompt(data, sample_size = 1):
    obs = sample_json_objects(data, sample_size)
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
    result = generate_prompt("test.json", 3)
    print(result)