import os

prj_folder = os.path.join(os.environ['USERPROFILE'], 'journal_app\\')
file_location = 'journal\\'
# file_location = 'application\\example44.txt'
file_path = prj_folder + file_location
# Get a list of all files and subdirectories in the specified folder
folder_contents = os.listdir(file_path)

# Filter the list to include only .txt files
txt_files = [file for file in folder_contents if file.endswith(".txt")]

# Print the list of .txt files
print("List of .txt files:")
for txt_file in txt_files:
    print(txt_file)
