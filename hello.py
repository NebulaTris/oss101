import os

def read_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
            print(f"Content of {file_path}:\n{content}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

def create_file(file_path, content):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as file:
            # Write content to the file
            file.write(content)
            print(f"File created at {file_path}")

    except Exception as e:
        print(f"Error creating file: {e}")

def update_file(file_path, new_content):
    try:
        # Open the file in append mode
        with open(file_path, 'a') as file:
            # Append new content to the file
            file.write("\n" + new_content)
            print(f"File updated at {file_path}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

def delete_file(file_path):
    try:
        # Remove the file
        os.remove(file_path)
        print(f"File deleted: {file_path}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example: Read, create, update, and delete a file
file_path = 'example.txt'
read_file(file_path)
create_file(file_path, 'Hello, this is a sample file content.')
update_file(file_path, 'This is additional content.')
read_file(file_path)
delete_file(file_path)
