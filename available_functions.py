from google import genai
from google.genai import types
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
        ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of the specified file, truncated to 10000 caracters and constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
        type=types.Type.STRING,
        description="The path of the file whose contents are to be retrieved.",
        ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the text contained in the contents argument to the specified file path, constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
        type=types.Type.STRING,
        description="The path of the file to be written to",
        ),
        "content": types.Schema(
            type=types.Type.STRING,
            description="The text to be written to the file"
        ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the a python file specified by the file_path parameter, with arguments specified by the args parameter, constrained to the working directory.",
    parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
        type=types.Type.STRING,
        description="The path of the python file to be executed.",
        ),
        "args": types.Schema(
        type=types.Type.STRING,
        description="The arguments to be passed to the call to the python interpreter. Defaults value is None.",
        ),
        },
    ),
)
    
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)