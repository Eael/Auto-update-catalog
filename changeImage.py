#! /usr/bin/env python3

import os
from PIL import Image
from glob import glob


def main():
    icons_directory = input("Input the directory where the icons are located: ") #C:/Users/teyee/Documents/PYTHON EARL/PythonAPI/images/
    save_directory = input("Input the directory where the resized icons are saved: ")


    for file in glob('{}/0*'.format(icons_directory)):
        path, filename = os.path.split(file)
        filename = os.path.splitext(filename)[0]
        image = Image.open(file).convert('RGB')
        image.resize((600,400)).save('{}{}.jpeg'.format(save_directory, filename))

    print('OK')


if __name__ == '__main__':
    main()
