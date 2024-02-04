
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


Oh, and here is another example of non-JSON stuff.
And here is JSON. It's valid again:

```json
{
  "domain": "Online Retail #2",
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