from dotenv import load_dotenv
import os
import json

load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_key = os.environ.get("CLIENT_KEY")