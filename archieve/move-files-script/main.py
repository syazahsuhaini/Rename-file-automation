# import modules needed
import os
from shutil import move

# making directories
root_dir = r"C:\Users\syaza\Downloads"
documents_dir = r"C:\Users\syaza\Downloads\documents"

# files types of the category
docs = ('.pdf')

# appending all the files in the root directory to files[]
files = []

print("📌 Scanning directory:", root_dir)
print("")

for f in os.listdir(root_dir):
    full_path = os.path.join(root_dir, f)
    print("Found:", f)
    if os.path.isfile(full_path) and not f.startswith('.'):
        print(" → Valid file added")
        files.append(f)
    else:
        print(" → Not a file, skipped")


# moving files to the respective folders,
# overwriting if needed
print("\n📌 Files collected:", files)

print("\n📌 Moving PDF files:\n")

for file in files:
    if file.endswith(docs):
        print(" → Moving:", file)
        # combines folder paths and filenames into a correct, complete path by
        # automatically chooses the right style depending on the system you’re running on
        move(os.path.join(root_dir, file), os.path.join(documents_dir, file))
        #print(f"Moved: {file}") 

print("\n✨ Done!")