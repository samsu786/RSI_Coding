import json
import httpx
import uuid
import os

SAMPLE_URL = "https://jsonplaceholder.typicode.com/posts"
FOLDER_PATH = "data"

def get_posts():
    try:
        with httpx.Client() as client:
            result =  httpx.get(SAMPLE_URL, timeout=10.0)
            if result.status_code == 200:
                json_data = result.json()
                with open(f"./{str(uuid.uuid4())}.json", "w") as f:
                    f.write(json.dumps(json_data))
    except Exceptions as e:
        return e

get_posts()