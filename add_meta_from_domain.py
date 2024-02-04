import json
import os
from glob import glob

def update_mappings(data_dir):
    for json_file in glob(os.path.join(data_dir, '*.json')):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        updated_data = []
        for item in data:
            # Check if item is a dict (single mapping) or list (multiple mappings)
            if isinstance(item, dict) and 'mapping' in item:
                if 'domain' in item and '_meta' not in item['mapping']:
                    item['mapping']['_meta'] = item['domain']
                updated_data.append(item)
            else:
                print(f"Unexpected entry: {item}")
        
        # Write the updated data back to the file
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(updated_data, file, ensure_ascii=False, indent=2)
        print(f"Updated file: {json_file}")

data_dir = "./data"  # Adjust this path to your data directory
update_mappings(data_dir)
