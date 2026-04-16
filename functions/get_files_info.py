import os

def get_files_info(working_directory, directory="."):
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
		valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
		if valid_target_dir == False:
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
		if os.path.isfile(target_dir) == True:
			return f'Error: "{directory}" is not a directory'
		files = os.listdir(target_dir)
		result = ""
		for file in files:\
			# print(f"{target_dir}/{file}")
			result += (f"- {file} : file_size={os.path.getsize(f"{target_dir}/{file}")}, is_dir={os.path.isdir(f"{target_dir}/{file}")}\n")
	except Exception as e:
		return f"Error: {e}"
	return result