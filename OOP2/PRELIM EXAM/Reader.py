import os
import json

def clear_screen():
    # 'nt' means Windows, 'posix' covers Linux and macOS
    os.system('cls' if os.name == 'nt' else 'clear')

def multiple_line_input(message=''):
    true_message = message + '(Enter "STOP" to stop): '
    lines = []
    while True:
        line = input(true_message)
        if line == "STOP":
            break
        lines.append(line)
    
    return "\n".join(lines)
    

class JSONFileReaderWriter():
    def read(self, filepath):
        with open(filepath, "r") as read_file:
            data = json.load(read_file)
            #print(data)
            return data

    def write(self, filepath, data):
        with open(filepath, "w") as write_file:
            json.dump(obj=data, fp=write_file)