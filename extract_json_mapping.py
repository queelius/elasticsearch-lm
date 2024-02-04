import json
from data_tool import DataTool
from extract_json import extract_json

objs = extract_json(output)

for obj in objs:
    data_tool = DataTool()
    valid = data_tool.validate_entry(obj)
    print(json.dumps(obj, indent=2))
