import json
import os
from glob import glob
from collections import defaultdict

class DataTool:
    def __init__(self):
        self.data = []

    def read(self, file_path: str) -> None:
        """
        Read JSON file into this object.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        print(f"Data read from {file_path}.")

    def merge(self, data_dir: str) -> None:
        """
        Merge all JSON files in data_dir into this object.
        """
        for file_path in glob(os.path.join(data_dir, '*.json')):
            with open(file_path, 'r', encoding='utf-8') as file:
                print(f"Reading {file_path}...")
                file_data = json.load(file)
                if not isinstance(file_data, list):
                    print(f"Unsupported data type in file: {file_path}")
                self.data.extend(file_data)
        print(f"Data merged.")

    def write(self, output_file: str) -> None:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            json.dump(self.data, outfile, ensure_ascii=False, indent=2)
        print(f"Data written to {output_file}.")

    def stats(self) -> None:
        """
        Some basic statistics
        """
        nlq_count = defaultdict(int)
        for entry in self.data:
            domain = entry["domain"]
            nlq_count[domain] += len(entry["NLQs"])
        print("NLQ count per domain:")
        for domain, count in nlq_count.items():
            print(f"{domain}: {count}")
        print(f"Total domains: {len(nlq_count)}")
        print(f"Total NLQs: {sum(nlq_count.values())}")

    def validate_entry(self, entry) -> bool:
        """
        Validate entry data.

        Here is the template for each entry in the data:

        ```
        {
            "domain": string,
            "mapping": {
                "properties": json_object,
                "_meta": json_object    
            },
            "NLQs": [
                {
                    "NLQ": string,
                    "query": json_object
                },
                ...
                {
                    "NLQ": string,
                    "query": json_object
                }
            ]
        }
        """

        print(f"Validating mapping")
        if not isinstance(entry, dict):
            print(f"Expected a dict type but got {type(entry)}: {entry}")
            return False

        if "domain" not in entry:
            print(f"Missing domain: {entry}")
            return False

        if "mapping" not in entry:
            print(f"Missing mapping: {entry}")
            return False

        if "NLQs" not in entry:
            print(f"Missing NLQs: {entry}")
            return False

        if not isinstance(entry["NLQs"], list):
            print(f"NLQs is not a list: {entry}")
            return False

        for nlq in entry["NLQs"]:
            if "NLQ" not in nlq:
                print(f"Missing NLQ: {nlq}")
                return False

            if "query" not in nlq:
                print(f"Missing query: {nlq}")
                return False

        print (f"Valid mapping: {entry['domain']=}")
        return True

    def validate(self) -> None:
        if not isinstance(self.data, list):
            print("Data is not a list.")
            return False

        valid = True
        for entry in self.data:
            valid = valid and self.validate_entry(entry)
        if valid:
            print("Data is valid.")
        else:
            print("Data is invalid.")

        return valid




