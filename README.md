# Rename-file-automation
A small automation tool using Python that will group certain downloaded files 
into their set folder and rename them to reduce manual file management.

## What this does and its current features
This tool helps organize frequently downloaded files by:
- Automatically moving selected files into a designated folder
- Renames files based on a predefined naming template and sequence

It is designed for simple, repeatable workflows where file naming consistency matters.

# How to run the script
1. Open a terminal and navigate to the project directory
2. For moving files into a folder, run: 
    ```bash 
    python script1.py
3. For renaming files, run: 
    ```bash
    python script2.py {month} {year}

# Demo
Video demonstration: https://youtu.be/ynXEx3kEoLs

# Future improvement
- Automatically detect month and year from file content
- Add argument parsing for cleaner CLI usage
- Combine scripts into a single CLI tool
- Package as a standalone executable