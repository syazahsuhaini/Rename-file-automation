# move the timesheet into timesheets folder

# importing required modules
import os
import sys
from shutil import move

from data_path import root_dir, timesheets_dir

def move_timesheet():

    # making sure the folder exists
    # parents=True means create all missing parent folders if doesnt exists
    # exist_ok=True means if folder exists then do nothing
    root_dir.mkdir(parents=True, exist_ok=True)
    timesheets_dir.mkdir(parents=True, exist_ok=True)

    # files types of each category
    docs = ('.pdf')

    # appending all the files in the root directory to files[]
    files = []

    print("\n📌 Scanning directory:", root_dir)
    print("")

    for f in os.listdir(root_dir):
        full_path = os.path.join(root_dir, f)
        if os.path.isfile(full_path) and not f.startswith('.') and f.startswith('timesheet_'):
            print("Found:", f)
            print(" → Timesheet added")
            files.append(f)

    print("\nTimesheet downloaded:", len(files))

    # moving files to the respective folders,
    # overwriting if needed
    print("\n📌 Moving PDF files:\n")

    for file in files:
        if file.endswith(docs):
            print(" → Moving:", file)
            move(os.path.join(root_dir, file), os.path.join(timesheets_dir, file))

    print("\n✨ Done!")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python rename.py")
        sys.exit(1)

    move_timesheet()