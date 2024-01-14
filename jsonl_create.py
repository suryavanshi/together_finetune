import os
import json



# Output JSON Lines file
out_file = 'langgraph.jsonl'

def read_py_files(dir_path):
    i = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                i+=1
                try:
                    with open(file_path) as f:
                        text = f.read()
                        if i<5:
                            print("file, text:",file_path, text)
                        if len(text)>100:
                            json_line = json.dumps({'text': text})
                            with open(out_file, 'a') as out:
                                out.write(json_line + '\n')
                            if i>200:
                                break
               
                except OSError:
                    pass # ignore errors opening files
    f.close()
start_dir = './langgraph' 
read_py_files(start_dir)