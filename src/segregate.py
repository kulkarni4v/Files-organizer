import os,shutil
def segregate(main_folder_path,files,file_types):
    for file in files:
      extension=file.split('.')[-1]
      if extension.lower() in file_types:
          src_path=os.path.join(main_folder_path,file)
          destination_path=os.path.join(main_folder_path,extension.upper())
          shutil.move(src_path,destination_path)