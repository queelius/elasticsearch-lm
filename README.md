# Fine-Tuning Language Models for API Query Generation

## Project Overview

This project aims to fine-tune a smaller Large Language Model (LLM) for the specific task of translating natural language queries (NLQs) into structured API queries, with an initial focus on Elasticsearch's Query DSL. The motivation behind this effort is to significantly enhance the accessibility and usability of API endpoints, making them more intuitive for users by allowing interactions in natural language.

The concept extends beyond Elasticsearch, proposing a universal approach to interfacing with various APIs. By leveraging compact, efficient language models, we envision a future where sophisticated API interactions are democratized, enabling more natural and user-friendly application interfaces.

## Motivation

While Large Language Models have demonstrated remarkable capabilities in understanding and generating natural language, their size and resource requirements often limit widespread deployment, especially in resource-constrained environments. This project explores the potential of smaller, optimized models to perform complex tasks—like generating accurate API queries from NLQs—while maintaining low latency, minimal memory footprint, and reduced power consumption. Such models can revolutionize API interactions across numerous platforms, making technology more accessible and intuitive for a broader user base.

## Objective

Fine-tune a small LLM, [TinyLlama](https://github.com/jzhang38/TinyLlama), to accurately translate NLQs into Elasticsearch JSON queries based on given Elasticsearch mappings. The project aims to showcase the efficiency and competency of the model at the task, with the objective of being able to place it in diverse environments, from serverless architectures to edge devices.

## Prior Work

This work is inspired by existing models that translate NLQs into SQL queries, like [duckdb-nsq](https://huggingface.co/motherduckdb/DuckDB-NSQL-7B-v0.1). We aim to build on this foundation by adapting the approach to the task of generating structured API queries, starting with Elasticsearch's Query DSL. The project also draws from research on fine-tuning language models for specific tasks, with a focus on optimizing model size and performance.

## Synthetic Data Generation

The foundation of our fine-tuning process involves creating a rich dataset of Elasticsearch [mappings (schemas)](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html), along with corresponding NLQs (natural language queries), and their target Elasticsearch JSON queries. This synthetic data is designed to cover a wide range of query types and complexities, ensuring that the model is trained on diverse examples that reflect real-world use cases.

This section details our approach to synthetic data generation, ensuring a broad coverage of query types and complexities.

We actually generated our synthetic data by first sampling from GPT-4, and then using those results to prime an open-source
model, [llama2](https://llama.meta.com/), to generate more synthetic data that was based on the high-quality examples
provided by GPT-4. This was done to ensure that the synthetic data was of high quality and covered a wide range of query types and complexities without costing too much in terms of computation resources. See the `synthetic_data_generation` directory for more details.

### Process

We use the very large and capable GPT-4 model to generate the synthetic data. The process involves three key steps:

1. **Generate Elasticsearch Mappings**: Create diverse mappings that represent different data domains, from e-commerce to public records.
2. **Generate NLQs**: For each mapping, develop a variety of natural language queries that reflect potential user intents.
3. **Generate Corresponding JSON Queries**: Construct accurate Elasticsearch queries for each NLQ, demonstrating the desired output for the model.

### JSON Format of Training Data

Each training example is a JSON object structured to contain all the necessary information for training the model to translate NLQs against mappings into the target Elasticsearch JSON queries.

This JSON format is designed for use in training machine learning models, specifically aimed at converting natural language queries into structured API queries when conditioned on Elasticsearch mappings. By documenting this JSON format, users and contributors can better understand how to create, extend, and utilize the synthetic dataset for training and testing purposes, ensuring that the data is correctly formatted and meaningful for the intended training tasks.

#### Structure

The JSON object for each training example comprises the following key components:

- **`domain`**: A string that identifies the specific domain or context of the example (e.g., "Healthcare Appointments", "Employee Attendance"). This helps in categorizing and filtering examples based on their application area.

- **`mapping`**: An object representing the Elasticsearch index mapping. This defines the schema of the data that the NLQ and query pertain to, including field names and their data types.

- **`NLQs`**: An array of objects, each containing:
  - **`NLQ`**: A string representing a natural language query. This is the query that a user might input, seeking information from the Elasticsearch index.
  - **`query`**: The Elasticsearch JSON query that corresponds to the `NLQ`. This object is structured according to the Elasticsearch Query DSL, representing the exact query that should be executed to satisfy the information need expressed in the `NLQ`.

##### Example

```json
{
  "domain": "Sample Domain",
  "mapping": {
    "properties": {
      "field1": { "type": "text" },
      "field2": { "type": "date" },
      "field3": { "type": "keyword" }
    }
  },
  "NLQs": [
    {
      "NLQ": "Example natural language query",
      "query": {
        "query": {
          "bool": {
            "must": [{ "match": { "field1": "some value" } }],
            "filter": [{ "range": { "field2": { "gte": "2023-01-01" } } }]
          }
        }
      }
    }
  ]
}
```

## Inference Time: The System Instruction

At inference time, users and developers are expected to use a `system instruction` that it is similar to the training data. The model will then generate a query that is similar to the `query` field in the training data. For example, in the above example, the system instruction is given by:

```json
{
  "domain": "Sample Domain",
  "mapping": { 
    "properties": {
      "field1": { "type": "text" },
      "field2": { "type": "date" },
      "field3": { "type": "keyword" }
    }
  },
}
```

Then, when the user asks the NLQ "Example natural language query", the program will
make this the prompt to the LLM, and the model will generate a response that
it has been fine-tuned to predict according to our synthetic training data.

#### In-Context Learning

There is also an opportunity for in-context learning, where the developers of the system can, given their special domain knowledge of their users and data, provide additional examples of NLQs and their corresponding queries.
However, since we are assuming computation resources are limited, adding to the context will generally slow down
the system. This is a tradeoff that the developers will have to make. Indeed, if resources are not that constrained, then
better results can be achieved by using a larger language model and optionally providing examples for in-context learning.

### Challenges and Solutions

- **Variability and Complexity**: Addressed by including a wide range of query scenarios and incorporating both basic and advanced Elasticsearch functionalities.
- **Realism**: Ensured by basing synthetic data on realistic use cases and varying the structure and complexity of mappings.

## Fine-Tuning Process

This section outlines the steps taken to adapt the language model to our specific task, including model selection, training environment setup, and evaluation metrics.

### Model Selection

Criteria for choosing a suitable smaller LLM include performance, efficiency, and adaptability to the task of generating structured API queries. This suggests looking for a model that has been fine-tuned on instruction following tasks, and that has a small memory footprint. The primary model we are considering is [TinyLlama](https://github.com/jzhang38/TinyLlama), which is a 1.1 billion parameter model that has been fine-tuned on instruction following tasks.

### Training and Evaluation

#### Dataset Preparation

We split the synthetic data into training, validation, and test sets, following a standard ratio (e.g., 70% training, 15% validation, 15% test). This ensures that the model is trained on a diverse range of examples and evaluated on unseen data.

#### Evaluation Metrics

Since we synthetically generated the data, there is no real data on which to evaluate the model. Hoewver, to make this problem more tractable, we consider the data in the test set as the ground truth. So, for the test set, we will take an additional step of generating more synthetic data for specifying the contents of the database for each mapping (domain). For each of these, we will have GPT-4 generate a Python script that populates the database with relevant values, and so we should be able to make these databases as large as we want without much time and effort.

We will then run the queries generated in the test set that correspond to each NLQ, by the model on the populated database, and then compare the search results from the model with the ground truth. In this way, even if the predicted query is different, as long as the search results are similiar (precision, recall, etc), we can consider the model to have performed well.

In information retrieval, the following metrics are commonly used:

- **Accuracy**: The proportion of search results that are relevant to the user's information need, as represented by the NLQ.
- **Precision**: The proportion of relevant search results among all retrieved results.
- **Recall**: The proportion of relevant search results that are retrieved among all relevant results.
- **Execution Success Rate**: The percentage of queries that are successfully executed. (The query may be malformed or invalid, leading to execution failure.)
    
## Future Directions

While the initial focus is on Elasticsearch, the methodology and findings from this project have broader implications. Future work will explore extending this approach to other APIs, further reducing model size without compromising performance, and investigating deployment strategies for real-time applications.

## Contributing

We welcome contributions from the community, whether it's in the form of feedback, bug reports, or pull requests.
