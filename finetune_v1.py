import os
import together
from dotenv import load_dotenv

load_dotenv()
together.api_key = os.environ["TOGETHER_API_KEY"]

train_file = "langchain_v2.jsonl"
resp = together.Files.check(file=train_file)
print("check1:",resp)

# resp_check = together.Files.check(file="langgraph.jsonl",model="mistralai/Mistral-7B-v0.1")
# print("data check:", resp_check)

resp_upload =together.Files.upload(file=train_file)
print("upload resp:", resp)
file_id = resp_upload["id"]
resp = together.Finetune.create(
  training_file = file_id,
  model = 'mistralai/Mistral-7B-v0.1',
  n_epochs = 3,
  n_checkpoints = 1,
  batch_size = 64, #this is global batch size, so 8 per GPU when 8 GPU's used
  learning_rate = 1e-5,
  suffix = 'mistral_langchain-finetune-b8',
  wandb_api_key = os.environ['WAND_API_KEY'],
)

fine_tune_id = resp['id']
print(resp)

# number of steps = num_tokens*epochs/(batch_szie*context)
# to list all finetune jobs - together finetune list
# to get number of train tokens - together finetune retrieve ft-d04e8568-b54a-493e-b99d-a95c1c2e8d6c
