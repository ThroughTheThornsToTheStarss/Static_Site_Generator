import shutil
import os

def clear_directory(path_base):
    if os.path.exists(path_base):
        shutil.rmtree(path_base)
    os.mkdir(path_base)

def copy_recursive(path_copy, path_base):

    files = os.listdir(path_copy)

    for el in files:
        full_path_copy = os.path.join(path_copy, el)
        full_path_base = os.path.join(path_base, el)

        if os.path.isfile(full_path_copy):
            shutil.copy(full_path_copy,full_path_base)

        else:
            os.mkdir(full_path_base)
            copy_recursive(full_path_copy, full_path_base)