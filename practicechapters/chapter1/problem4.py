import os

# Specify the directory path (use '.' for the current directory)
directory_path = '/'

try:
    # Retrieve the contents of the directory
    directory_contents = os.listdir(directory_path)
    
    print(f"Contents of '{directory_path}':")
    for item in directory_contents:
        print(item)
        
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")