import re
import sys
import subprocess

subprocesses = []


def run_subprocess(command):
    try:
        subprocess_obj = subprocess.Popen(command)
        subprocesses.append(subprocess_obj)
        subprocess_obj.wait()
    except Exception as e:
        print(f"Error running subprocess: {str(e)}")


if __name__ == "__main__":
    try:
        while True:
            user_input = input("Write Command: ")
            if user_input.lower().startswith('create'):
                command = ['python3', 'create.py'] + \
                    user_input[len('create'):].strip().split()
                run_subprocess(command)
            elif user_input.lower().startswith('insert'):
                command = ['python3', 'insert.py'] + \
                    user_input[len('insert'):].strip().split()
                run_subprocess(command)
            elif user_input.lower().startswith('update'):
                command = ['python3', 'update.py'] + \
                    user_input[len('update'):].strip().split()
                run_subprocess(command)
            elif user_input.lower().startswith('delete'):
                command = ['python3', 'delete.py'] + \
                    user_input[len('delete'):].strip().split()
                run_subprocess(command)
            elif user_input.lower() == 'exit':
                break
    finally:
        for subprocess_obj in subprocesses:
            subprocess_obj.terminate()
