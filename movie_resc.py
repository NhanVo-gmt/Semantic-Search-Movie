import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

mongo_password = os.getenv("MONGO_PASSWORD")
client = pymongo.MongoClient(f"mongodb+srv://tonynhanvo:{mongo_password}@cluster0.yuaggbs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.sample_mflix
collection = db.movies

hf_token = os.getenv("HF_TOKEN")
model_id = os.getenv("MODEL_ID")
embedding_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"

items = collection.find().limit(5)
for item in items:
    print(item)
