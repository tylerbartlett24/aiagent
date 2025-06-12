import os
from pathlib import Path 

def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    
        if not abs_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        output_file = Path(abs_path)
        output_file.parent.mkdir(exist_ok=True, parents=True)
        with open(output_file, "w") as file:
            file.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error writing to {file_path}: {e}'