import os
import json
from pathlib import Path

import nbformat

def process_dir(dir_path, output_file):
    for path in Path(dir_path).rglob('*.py'):
        with open(path) as f:
            content = f.read()
        output_file.write(json.dumps({'text': content}) + '\n')

    for path in Path(dir_path).rglob('*.ipynb'):
        nb = nbformat.reads(path.read_bytes(), nbformat.NO_CONVERT)
        code = ''
        for cell in nb.cells:
            if cell.cell_type == 'code':
                code += cell.source + '\n'
        output_file.write(json.dumps({'text': code}) + '\n')
    
    for path in Path(dir_path).rglob('*.mdx'):
        with open(path) as f:
            content = f.read()
        output_file.write(json.dumps({'text': content}) + '\n')

output_path = 'langchain_v2.jsonl'
with open(output_path, 'w') as f:
    process_dir('./langgraph', f)