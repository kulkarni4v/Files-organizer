import os

def folder_creation(path,files):

    for file in files:
        capitalized_file=file.upper()

        folders_path=os.path.join(path,capitalized_file)
        if os.path.exists(folders_path):
            pass
        else:
            os.mkdir(folders_path)
