#!/usr/bin/env python3
# Author ID: 133245233

def read_file_string(file_name):
    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines = f.read().splitlines()
    return lines
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))