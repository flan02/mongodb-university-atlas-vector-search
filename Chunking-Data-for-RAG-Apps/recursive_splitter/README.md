# Recursive Text Splitter PDF Demo

This demo shows how to create chunks of a PDF document using Langchain's `RecursiveCharacterTextSplitter` method and add them to a new collection in an MongoDB Atlas Cluster with vector embeddings. 

## Prerequisites

- Atlas Cluster Connection String
- Open AI API Key

## Setup

Install the requirements:

```bash
pip3 install langchain langchain_community langchain_openai pymongo pypdf python-dotenv
```

Add your Connection String and LLM API Key to the `.env` file.


## Usage

This demo includes a sample PDF in the `sample_files` directory that is ready to use. You can optionally add your own PDF to the folder.

Run the demo:

```bash
python3 recursive_splitter.py
```
