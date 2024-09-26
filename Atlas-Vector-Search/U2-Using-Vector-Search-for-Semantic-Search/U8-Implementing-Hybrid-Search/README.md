# Implementing Hybrid Search

This demo shows how to implement hybrid search using an Aggregration pipeline to combine Atlas Vector Search and full-text search. 

## Prerequisites

- Atlas Cluster Connection String
- OpenAI API Key
- Sample Datasets loaded into Atlas Cluster

## Setup

Install the requirements:

```bash
pip install pymongo requests python-dotenv
```

Create an `.env` file with the following content:

```bash
OPENAI_API_KEY=""
MONGODB_URI=""
```

**Note:** Replace the `MONGODB_URI` and `OPENAI_API_KEY` values with your own values.

Load the `sample_mflix` dataset into your Atlas Cluster.

Create the following vector search index on the `embedded_movies` collection in your Atlas Cluster:

```bash
{
  "fields": [
    {
      "numDimensions": 1536,
      "path": "plot_embedding",
      "similarity": "cosine",
      "type": "vector"
    }
  ]
}
```

**Note:** Name the index `vectorPlotIndex`.

## Usage

Update the `query` variable in the `hybrid_search.py` file by passing in a question:

```python
query = "A movie that is about people who are trying to escape from a maximum security facility."
```

Run the demo:

```bash
python hybrid_search.py
```
