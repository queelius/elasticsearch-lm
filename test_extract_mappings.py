import json
from data_tool import DataTool
from extract_json import extract_json
from os import path

with open("example.md", 'r', encoding='utf-8') as file:
  text = file.read()
  objs = extract_json(text)
  print("Extracted Elasticsearch mappings:") 
  for obj in objs:
      data_tool = DataTool()
      valid = data_tool.validate_entry(obj)
