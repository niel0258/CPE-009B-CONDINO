import os
import json

#Better format
def clear_screen():
    # 'nt' means Windows, 'posix' covers Linux and macOS
    os.system('cls' if os.name == 'nt' else 'clear')


#For multiple lines of input
def multiple_line_input(message=''):
    true_message = message + '(Enter "STOP" to stop): '
    lines = []
    while True:
        line = input(true_message)
        if line == "STOP":
            break
        lines.append(line)
    
    return "\n".join(lines)
    
#For importing and exporting on a json file
class JSONFileReaderWriter():
    def read(self, filepath):
        try:
            with open(filepath, "r") as read_file:
                data = json.load(read_file)
                #print(data)
                return data
        #Fallback in case no file is found
        except FileNotFoundError:
            return []

    def write(self, filepath, data):
        with open(filepath, "w") as write_file:
            json.dump(obj=data, fp=write_file,indent=4)