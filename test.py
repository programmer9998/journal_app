import os

# this is the folder when the .exe file and its dependent files are located.
# prj_folder = 'C:\\Users\TubePrinter\\ai_printer\\application\\'
prj_folder = os.path.join(os.environ['USERPROFILE'], 'journal_app\\')
file_location = 'journal\\example.txt'
file_location = 'application\\example44.txt'
file_path = prj_folder + file_location

'''
# Open the file in write mode
with open(file_path, "w") as file:
    # Write content to the file
    file.write("Hello, world!\n")
    file.write("This is a new file created u2sing23232 Python.\n")

print(f"File '{file_path}' created successfully.")

'''


# Open the file in read mode
with open(file_path, "r") as file:
    # Read the contents of the file
    file_contents = file.read()

print(f"Contents of '{file_path}':\n{file_contents}")