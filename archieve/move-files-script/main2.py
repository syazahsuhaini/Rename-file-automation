# tutorial: https://www.geeksforgeeks.org/python/automate-renaming-and-organizing-files-with-python/
# importing required modules
import os
from shutil import move

# making the directories
root_dir = "C:\\Users\\syaza\\Downloads"
documents_dir = "C:\\Users\\syaza\\Downloads\\documents"

# files types of each category
docs = ('.pdf')


# appending all the files in the root directory to files[]
files = []
for f in os.listdir(root_dir):

    if os.path.isfile(f) and not f.startswith('.') and not f.__eq__(__file__):
        files.append(f)

"""
f.__eq__(__file__) equivalent to f == __file__

f >> filename from Downloads
__file__ >> special built-in var in python, filename/path of the script being executed
"""

# moving files to the respective folders,
# overwriting if needed
for file in files:
    if file.endswith(docs):
        move(file, documents_dir+"/"+file)
        # the above only work if the current directory is Downloads folder
        # the file append part is only append the file name, it will be used in here
        # by finding the file with name listed in the list and move it to the new directory