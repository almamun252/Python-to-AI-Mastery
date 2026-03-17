import os

# view Current Working Directory 
current_path = os.getcwd()
print(f"Current Directory: {current_path}")

# view all files and folders in current directory (os.listdir)
# '.' means current directory
files_and_folders = os.listdir('.')
print("\nItems in current directory:")
for item in files_and_folders:
    print(f"- {item}")

# using os.path.abspath() to get the absolute path of the current directory
current_path_absolute = os.path.abspath('.')
print(f"\nAbsolute Path of Current Directory: {current_path_absolute}")

# if my_new_folder doesn't exist, create it. Otherwise, print that it already exists.
folder_name = "my_new_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"\nFolder '{folder_name}' created successfully!")
else:
    print(f"\nFolder '{folder_name}' already exists.")

# ৪. OS-independent file path creation (os.path.join)
# this will create a file path that works on any operating system (Windows, Linux, Mac)
new_file_path = os.path.join(folder_name, "test_file.txt")
print(f"\nSafe File Path: {new_file_path}")