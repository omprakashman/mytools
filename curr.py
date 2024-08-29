import os
import glob
from datetime import datetime
# OM Commit A

# Define the source directories
source_directory_1 = r'C:\Users\OMCENTER\projects\mytools\simplelogin\droid'
source_directory_2 = r'C:\Users\OMCENTER\projects\mytools\simplelogin\authapp'

# Define the destination file
destination_file = r'C:\Users\OMCENTER\Desktop\driodworks.txt'

# Open the destination file in write mode
with open(destination_file, 'w') as dest_file:
	# Get the current date and time
	current_datetime = datetime.now().strftime("%b %d, %y %I:%M %p")
	# Write the header with the current date and time
	dest_file.write(f"Django Text File  :  {destination_file} On Date @ Time {current_datetime} >>\n\n")

	# Loop 1: Find all .py files in the first source directory
	py_files_1 = glob.glob(os.path.join(source_directory_1, '*.py'))

	# Loop through each .py file in the first source directory
	for py_file in py_files_1:
		# Add the file name before the content
		file_name = os.path.basename(py_file)
		dest_file.write(f"<<****** Python file project directory :  {file_name} **********>>\n")
		
		# Open and read the content of the .py file
		with open(py_file, 'r') as file:
			content = file.read()
			# Append the content to the destination file
			dest_file.write(content)
			dest_file.write('\n\n')  # Add a newline for separation between files

	# Loop 2: Find all .py files in the second source directory
	py_files_2 = glob.glob(os.path.join(source_directory_2, '*.py'))

	# Loop through each .py file in the second source directory
	for py_file in py_files_2:
		# Add the file name before the content
		file_name = os.path.basename(py_file)
		dest_file.write(f"<<****** Python file app directory :  {file_name} **********>>\n")
		
		# Open and read the content of the .py file
		with open(py_file, 'r') as file:
			content = file.read()
			# Append the content to the destination file
			dest_file.write(content)
			dest_file.write('\n\n')  # Add a newline for separation between files