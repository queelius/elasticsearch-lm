import json
from data_tool import DataTool
from extract_json import extract_json

example_text = """

Here is an example of non-JSON stuff.

```json
{
  "domain": "Online Retail",
  "mapping": {
    "properties": {
      "product_id": { "type": "keyword", "description": "Unique identifier for each product." },
      "name": { "type": "text", "description": "Name of the product." }
    },
    "_meta": "This mapping allows for filtering products by name, availability, and categories in search queries." 
  }
}
```

Here is another example of non-JSON stuff.

Now we have some more JSON, but invalid...

```json
{
  "NLQs": 
    {
      "NLQ": "What products are available?",
      "query": {
        "match_all": {}
      }
    },
    {
      "NLQ": "Show me all products with 'apple' in the name.",
      "query": {
        "match": {
          "name": "apple"
        }
      }
    }
  ]
}
```

And finally, here is a valid JSON block.
    
```json
{
"domain": "Online Retail",
"mapping": {
    "properties": {
    "product_id": { "type": "keyword", "description": "Unique identifier for each product." },
    "name": { "type": "text", "description": "Name of the product." }
    },
    "_meta": "This mapping allows for filtering products by name, availability, and categories in search queries." 
},
"NLQs": [
    {
    "NLQ": "What products are available?",
    "query": {
        "match_all": {}
    }
    },
    {
    "NLQ": "Show me all products with 'apple' in the name.",
    "query": {
        "match": {
        "name": "apple"
        }
    }
    }
]
}
``` 
"""

extracted_json_objects = extract_json(example_text)

# Printing extracted JSON objects
#for obj in extracted_json_objects:
#    print(json.dumps(obj, indent=2))

# Now let's use validate_data.py to validate the extracted JSON objects
    
for obj in extracted_json_objects:
    data_tool = DataTool()
    valid = data_tool.validate_entry(obj)
    print("Valid:" if valid else "Invalid:")
    print(json.dumps(obj, indent=2))
    print("*" * 20)