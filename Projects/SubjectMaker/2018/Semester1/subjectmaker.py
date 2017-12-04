from shutil import copy2
import os, errno


subjects = []
folders = []

with open("folders.txt") as folders_file:
    for folder in folders_file:
        folders.append(folder.strip('\r\n'))

with open("subjects.txt") as subject_file:
    for subject in subject_file:
        subjects.append(subject.strip("\r\n"))

def make_subject_folder(subject):
    try:
        os.makedirs(subject)
        for folder in folders:
            os.makedirs(f"{subject}/{folder}")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

for subject in subjects:
    make_subject_folder(subject)
    copy2('UbD_Template.docx', f'{subject}/000_Admin/UbD_{subject}.docx')
