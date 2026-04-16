import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
		valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

		if valid_target_file is False:
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

		if os.path.isdir(target_file):
			return f'Error: "{file_path}" does not exist or is not a regular file'

		if target_file.endswith(".py") == False:
			f'Error: "{file_path}" is not a Python file'

		command = ["python", target_file]

		for arg in args.split():
			command.extend(arg)
		
		subprocess()
	except Exception as e:
		return f"Error: {e}"

	return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

