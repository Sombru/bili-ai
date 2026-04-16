import os

def write_file(working_directory, file_path, content):
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
		valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
		# print(target_file)
		if valid_target_file == False:
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
		if os.path.isfile(target_file) == False:
			return f'Error: Cannot write to "{file_path}" as it is a directory'
		
	except Exception as e:
		print("Error:", e); 
	return content

