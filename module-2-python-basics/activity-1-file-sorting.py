"""
Module 2 — Activity: File Sorting with os and shutil
Student: Chanel Jeraldine M. Fernandez
Date: 9/25/2026

============================================
WHAT DID YOU BUILD? (explain in your own words)
============================================
I created a simple python file script that automatically
sorts files into different folders based on their file extensions.
Example, .jpg and .png files are place in an images folder, while
.docx and .pdf belongs in the Documents folders. This will lessen
thw need to manually move each file and helps keep the fils organize.


============================================
KEY VOCABULARY
============================================
- os module: this is used to work with files and folders
- shutil module: To move or copy files
- file path: Location of file
- directory: A folder where files are stored
- file extension: shows the type of the file, .jpg or .pdf
(add more as needed)


============================================
YOUR SCRIPT
============================================
Paste the code you already wrote for this activity below.
"""

import os
import shutil

source_folder = "files"

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if filename.endswith(".jpg") or filename.endswith(".png"):
        folder = "Images"
    elif filename.endswith(".pdf") or filename.endswith(".docx"):
        folder = "Documents"
    else:
        continue

    destination = os.path.join(source_folder, folder)
    os.makedirs(destination, exist_ok=True)

    shutil.move(file_path, os.path.join(destination, filename))

print("Files organized successfully!")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I want to avoid is using a file path that does not exist. 
If the source folder is incorrect, it will not work or able to find
the file and also i need to make sure that files are not accicentally
moved to the wrong folder.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This is similar to real automation because a computer can automatically perform
repetitive task instead of doing them manually. Ex. a similar script can recognize school files
such as assignment, records, grades and such, this can save time, esp when there are many files to
manage.
