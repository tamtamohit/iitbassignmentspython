import tarfile
import os

import sys


class Question1TarFile:
    def __init__(self, path_to_compressed_file, path_to_original_file):
        if os.path.isfile(path_to_original_file):
            self.path_to_original_file = path_to_original_file
        else:
            return print("Error: File not found, please give absolute path to the file.")

        if os.path.isdir(os.path.split(path_to_compressed_file)[0]):
            self.path_to_compressed_file = path_to_compressed_file
        else:
            return print(
                "Error: Invalid folder name. Folder not found to compressed file. Folder names are case sensitive, please check the folder name.")
        self.compress_file()

    def compress_file(self):
        with tarfile.open(self.path_to_compressed_file, 'w') as tar:
            tar.add(self.path_to_original_file)
        print('Objective Completed')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error:  Too less argument.")
    else:
        ob = Question1TarFile(sys.argv[1],sys.argv[2])
