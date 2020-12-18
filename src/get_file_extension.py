import os
def get_file_extensions(path):
    files = os.listdir(path)
    diff_file_types = []
    diff_files=[]
    for file in files:
        print(file)

        file_subitems = file.split('.')
        if len(file_subitems) > 1:
            diff_files.append(file)
            file_extension = file_subitems[-1]
            diff_file_types.append(file_extension)
    return set(diff_file_types),diff_files