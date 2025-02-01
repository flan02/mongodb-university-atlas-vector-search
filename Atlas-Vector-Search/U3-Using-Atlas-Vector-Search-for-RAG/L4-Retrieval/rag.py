from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
import key_param

dbName = "book_mongodb_chunks"
collectionName = "chunked_data"
index = "vector_index"

vectorStore = MongoDBAtlasVectorSearch.from_connection_string(
    key_param.MONGODB_URI,
    dbName + "." + collectionName,
    OpenAIEmbeddings(disallowed_special=(), openai_api_key=key_param.LLM_API_KEY),
    index_name=index
)

def query_data(query):
    retriever = vectorStore.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3,
            # "pre_filter": { "hasCode": { "$eq": False } },
            # "score_threshold": 0.01
        },
    )

    results = retriever.invoke(query)
    print(results)

    

query_data("When did MongoDB begin supporting multi-document transactions?")
