import os
import pinecone

# initialize connection to pinecone (get API key at app.pinecone.io)
api_key = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"
# find your environment next to the api key in pinecone console
env = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"

pinecone.init(api_key=api_key, environment=env)

index_name = 'gpt-4-langchain-docs-fast'

import time

# check if index already exists (it shouldn't if this is first time)
if index_name not in pinecone.list_indexes():
    # if does not exist, create index
    pinecone.create_index(
        index_name,
        dimension=1536,  # dimensionality of text-embedding-ada-002
        metric='cosine'
    )
    # wait for index to be initialized
    time.sleep(1)

# connect to index
index = pinecone.GRPCIndex(index_name)
# view index stats
print(index.describe_index_stats())
