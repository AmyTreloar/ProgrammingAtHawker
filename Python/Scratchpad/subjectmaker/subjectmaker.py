import os

root_folders = [
    '.admin',
    '.documents',
    '.purchases',
    '.reporting',
    '.resources',
]

subjects = [
    'Engineering',
    'Programming11',
    'Programming12',
    'Robotics'
]

sub_folders = [
    '000_admin',
    '001_unit_outline',
    '002_weekly_content',
    '003_learning_briefs',
    '004_assessment_items',
    '999_other'
]

for folder in root_folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"directory {folder} created")
    else:
        print(f'directory {folder} already exists')

for subject in subjects:
    for sub_folder in sub_folders:
        path = f"{subject}/{sub_folder}"
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"directory {path} created")
        else:
            print(f'directory {path} already exists')