schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file in a specified directory relative to the working directory, providing file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path for a file to read contents of, relative to the working directory",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file in a specified directory relative to the working directory with given arguments, returns output of a program as a string",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to a pyhotn file to run, relative to the working directory",
            ),
            "args": types.Schema(
           	    type=types.Type.ARRAY,
                description="Command line arguments for a python script, default is None",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file in a specified directory relative to the working directory, returns a string wich indicates if operation was a success",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path for a file to write to, relative to the working directory",
            ),
            "contents": types.Schema(
                type=types.Type.STRING,
                description="Data which shoul be written to a file",
            ),
        },
    ),
)