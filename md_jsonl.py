import os
import re
import json
from pathlib import Path

import nbformat

def clean_text(text):
    regex = re.compile(r'\\u[a-fA-F0-9]{4}')
    cleaned_text = "" 
    prev_end = 0
    for match in regex.finditer(text):
        start, end = match.span()
        cleaned_text += text[prev_end:start]
        prev_end = end
    cleaned_text += text[prev_end:]
    return cleaned_text

def process_dir(dir_path, output_file):

    for path in Path(dir_path).rglob('*.mdx'):
        with open(path) as f:
            content = f.read()
        # content = re.sub(r'\\u[a-fA-F0-9]{4}', '', content) 
        # content = clean_text(content)
        output_file.write(json.dumps({'text': content}) + '\n')

output_path = 'langchain_docs.jsonl'
with open(output_path, 'w') as f:
    process_dir('./langchain/docs/docs/get_started', f)