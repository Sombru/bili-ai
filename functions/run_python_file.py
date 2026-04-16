import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
		valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

		if valid_target_file is False:
			return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

		if os.path.isfile(target_file) == False:
			return f'Error: "{file_path}" does not exist or is not a regular file'

		if target_file.endswith(".py") == False:
			return f'Error: "{file_path}" is not a Python file'

		command = ["python", target_file]

		if args is not None:
			for arg in args:
				command.extend(arg)
		
		stdout = ""
		stderr = ""
		res = ""
		process = subprocess.run(command, text=True, timeout=30)
		if process.returncode != 0:
			res += f"Process exited with code {process.returncode}"
		if process.stderr == "" and process.stdout == "":
			res += "No output produced"
		else:
			res += f"STDOUT: {process.stdout}"
			res += f"STDERR: {process.stderr}"
	except Exception as e:
		return f"Error: executing Python file: {e}"

	return res

