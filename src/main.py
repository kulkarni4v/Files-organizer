from src.get_file_extension import get_file_extensions
from src.create_folders import folder_creation
from src.segregate import segregate
path = "D:\sample"

file_types, diff_files = get_file_extensions(path)
folder_creation(path, file_types)
segregate(main_folder_path=path, files=diff_files, file_types=file_types)