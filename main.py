import re
import sys
import subprocess

if __name__ == "__main__":
    while True:
        user_input = input("Write Command: ")
        if user_input.lower().startswith('create'):
            command = user_input[len('create'):].strip()
            subprocess.run(['python3', 'create.py', command])
        elif user_input.lower().startswith('insert'):
            command = user_input[len('insert'):].strip()
            subprocess.run(['python3', 'insert.py', command])
        elif user_input.lower().startswith('update'):
            command = user_input[len('update'):].strip()
            subprocess.run(['python3', 'update.py', command])
        elif user_input.lower().startswith('delete'):
            command = user_input[len('delete'):].strip()
            subprocess.run(['python3', 'delete.py', command])
        elif user_input.lower().startswith('aggregate'):
            command = user_input[len('aggregate'):].strip()
            subprocess.run(['python3', 'aggregate.py', command])
        elif user_input.lower().startswith('select'):
            command = user_input[len('select'):].strip()
            subprocess.run(['python3', 'Select.py', command])
        elif user_input.lower() == 'exit':
            break
