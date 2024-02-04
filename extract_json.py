import json
import re
import sys

def extract_json(text):
    """
    Extracts JSON strings from text and returns them as Python dictionaries.
    
    Args:
    - text (str): The input text containing JSON objects in code blocks.
    
    Returns:
    - List[dict]: A list of Python dictionaries parsed from the JSON strings found in the text.
    """
    json_objects = []
    # Regular expression pattern to find JSON blocks
    pattern = r'```json\n([\s\S]*?)\n```'
    matches = re.findall(pattern, text)

    for match in matches:
        try:
            # Convert the matched JSON string to a Python dictionary and append to the list
            json_obj = json.loads(match)
            json_objects.append(json_obj)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    
    return json_objects


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: extract_json.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        objs = extract_json(text)
        with open('output.json', 'w') as f:
            json.dump(objs, f, indent=2)