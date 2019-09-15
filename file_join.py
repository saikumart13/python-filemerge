import os
from datetime import datetime

def get_files(path):
    """Returns the name, creation time of the .txt files in the given path"""
    try:
        os.chdir(path)
        txt_files = {}
        files = os.listdir(path)

        for file in files:
            if file.split('.')[-1] == 'txt':
                txt_files[file] = datetime.fromtimestamp(os.stat(os.path.join(path, file)).st_ctime)
        return txt_files
    except FileNotFoundError:
        print('Check the entered file path...')


def merge_files(txt_files):
    """Creates a new file by merging other files

    It copies all the text files that were created today and appends to a new file"""
    new_file = str(datetime.today().date()) + '_unified.txt'
    for a in txt_files:
        if txt_files[a].date() == datetime.today().date() and a != new_file:
            print(a)
            with open(new_file, 'a+') as out, open(a, 'r') as inp:
                line = inp.readline()
                while line:
                    out.write(line)
                    line = inp.readline()
    return new_file


path = input('Enter the directory path: ')
new_file = merge_files(get_files(path))
try:
    with open(new_file, 'r') as out:
        print(out.readline())
except:
    print('No text files created today')


