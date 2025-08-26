from pinecone import Pinecone, Index, ServerlessSpec
from pinecone.exceptions import PineconeApiException
from config.config import PINECONE_API_KEY, PINECONE_INDEX_NAME, PINECONE_ENVIRONMENT, PINECONE_CLOUD
import time

class PineconeClient:
    def __init__(self, index_name=PINECONE_INDEX_NAME, dimension=768):
        # Pass api_key, environment explicitly
        self.pc = Pinecone(
            api_key=PINECONE_API_KEY,
            environment=PINECONE_ENVIRONMENT
        )
        self.index_name = index_name
        self.dimension = dimension
        self.index: Index = self._get_or_create_index()

    def _get_or_create_index(self):
        try:
            existing_indexes = self.pc.list_indexes().names()
        except PineconeApiException as e:
            print(f"Error listing Pinecone indexes: {e}")
            print("Please check your Pinecone API key and network connection.")
            raise

        if self.index_name not in existing_indexes:
            print(f"Creating Pinecone index: {self.index_name}")
            try:
                self.pc.create_index(
                    name=self.index_name,
                    dimension=self.dimension,
                    metric="cosine",
                    spec=ServerlessSpec(cloud=PINECONE_CLOUD, region=PINECONE_ENVIRONMENT)
                )
                print(f"Index '{self.index_name}' created. Waiting for it to be ready...")
                while not self.pc.describe_index(self.index_name).status['ready']:
                    time.sleep(1)
                print(f"Index '{self.index_name}' is ready.")
            except PineconeApiException as e:
                print(f"Error creating Pinecone index '{self.index_name}': {e}")
                print("This might be due to free-tier limits, an invalid API key, or a region issue.")
                raise
        else:
            print(f"Pinecone index '{self.index_name}' already exists.")
            try:
                if not self.pc.describe_index(self.index_name).status['ready']:
                    print(f"Index '{self.index_name}' is not yet ready. Waiting...")
                    while not self.pc.describe_index(self.index_name).status['ready']:
                        time.sleep(1)
                    print(f"Index '{self.index_name}' is now ready.")
            except PineconeApiException as e:
                print(f"Error describing Pinecone index '{self.index_name}': {e}")
                print("Please check your Pinecone index status in the console.")
                raise

        return self.pc.Index(self.index_name)

    def upsert_vectors(self, vectors: list):
        if not vectors:
            print("No vectors to upsert.")
            return
        try:
            self.index.upsert(vectors=vectors)
            print(f"Upserted {len(vectors)} vectors to Pinecone index '{self.index_name}'.")
        except PineconeApiException as e:
            print(f"Error upserting vectors to Pinecone: {e}")
            print("Please ensure the index is ready and vector dimensions/format are correct.")
        except Exception as e:
            print(f"An unexpected error occurred during upsert: {e}")

    def query_vectors(self, query_embedding: list, top_k: int = 3) -> list:
        try:
            results = self.index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
            return results.matches
        except PineconeApiException as e:
            print(f"Error querying Pinecone: {e}")
            print("Please check your Pinecone API key, index status, and query parameters.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred during query: {e}")
            return []

    def delete_all_vectors(self):
        try:
            self.index.delete(delete_all=True)
            print(f"All vectors deleted from index: {self.index_name}")
        except PineconeApiException as e:
            print(f"Error deleting all vectors from Pinecone: {e}")
            print("This can happen if the index is not found or other API issues.")
        except Exception as e:
            print(f"An unexpected error occurred during full index delete: {e}")
