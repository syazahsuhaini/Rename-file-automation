# rename the timesheets into:
# TIMESHEET SYAZA HAZWANI BINTI SUHAINI [MONTH] [YEAR] [WEEK] FIELDGLASS
# each timesheet have their own ID. the bigger the ID, the later the dates
# constant name: timesheet_MFCTSxxxxxxxx.pdf where xxxxxxxx is the changeable number in ID

# sort the files based on their name
# then rename the files

# importing required modules
import os
import sys

from data_path import timesheets_dir

def rename_timesheet(month, year):

    # save the files name into a list then sort it based on their name
    files = []

    print("\n📌 Scanning directory:", timesheets_dir)
    print("")

    for f in os.listdir(timesheets_dir):
        full_path = os.path.join(timesheets_dir, f)
        if os.path.isfile(full_path) and not f.startswith('.') and f.startswith('timesheet_'):
            print("Found:", f)
            print(" → Timesheet added")
            files.append(f)
        else:
            print("Clear the file in timesheets folder")

    sorted_files = sorted(files)
    counted_files = len(files)

    # rename files
    for counted_files, file in enumerate(files, start=1):
        new_name = f"SYAZA HAZWANI BINTI SUHAINI {month} {year} W{str(counted_files)} FIELDGLASS.pdf"
        new_name = os.path.join(timesheets_dir, new_name)
        ori_name = os.path.join(timesheets_dir, file)
        os.rename(ori_name, new_name)
        print(f"File renamed from '{ori_name}' to '{new_name}' successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rename.py <MONTH> <YEAR>")
        sys.exit(1)

    month = sys.argv[1].upper()
    year = sys.argv[2]

    rename_timesheet(month, year)