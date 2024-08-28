# Preparing The Data Demo

This demo shows how to prepare a PDF for use with a Retrieval Augmented Generation (RAG) system. The PDF is split into chunks and stored in an Atlas Cluster. The chunks are then indexed using Atlas Vector Search. The indexed chunks can be used to retrieve relevant information for a given query. 

## Prerequisites

- Atlas Cluster Connection String
- OpenAI API Key

## Usage

Install the requirements:

```bash
pip3 install langchain langchain_community langchain_core langchain_openai langchain_mongodb pymongo pypdf
```

Create a `key_param` file with the following content:

```python
MONGODB_URI=<your_atlas_connection_string>
LLM_API_KEY=<your_llm_api_key>
```

**Note:** Replace the `MONGODB_URI` and `LLM_API_KEY` values with your own values.

Load the sample data into your Atlas Cluster:

```bash
python load_data.py
```

