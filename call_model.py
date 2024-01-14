
import os
import together
from dotenv import load_dotenv

load_dotenv()
together.api_key = os.environ["TOGETHER_API_KEY"]


output = together.Complete.create(
  prompt = "//Build a chatbot using langcahin/ndef bot():",  
  model = "my_email/Mistral-7B-v0.1-mistral_langgraph-finetune-2024-01-14-00-18-04", 
  max_tokens = 256,
  temperature = 0.8,
  top_k = 60,
  top_p = 0.6,
  repetition_penalty = 1.1,
  stop = []
)

print("Fine tune output:",output)