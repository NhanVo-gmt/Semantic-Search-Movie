import pymongo
from dotenv import load_dotenv
import os
import requests

load_dotenv()

mongo_password = os.getenv("MONGO_PASSWORD")
client = pymongo.MongoClient(f"mongodb+srv://tonynhanvo:{mongo_password}@cluster0.yuaggbs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

hf_token = os.getenv("HF_TOKEN")
model_id = os.getenv("MODEL_ID")
embedding_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"

def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    if (response.status_code != 200):
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# for doc in collection.find({'plot':{"$exists": True}}).limit(50):
#     doc['plot_embedding_hr'] = generate_embedding(doc['plot'])
#     collection.replace_one({'_id': doc['_id']}, doc)

query = "imaginary characters from outer space at war"

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding_hr",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
    
