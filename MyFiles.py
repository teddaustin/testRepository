"""
Initialize
    and import
"""
import sys
import csv
import os
import timeit
import fileinput
import os.path
import glob
import numpy as np
import pandas as pd
from FileObject import FileClass
# import random

def recursively_find_ext(topdir,exten):

    counter = 0
    #one dim array of strings with max of 20 elements
    FileList = [[' ' for _ in range(1)] for _ in range(20)]
    for dirpath, dirnames, files in os.walk(topdir):
        #print('0:',dirpath,'1:',dirnames,'2:',files)
        for name in files:
            if name.lower().endswith(exten):
                FileList [counter] = name
                counter += 1

    if counter == 0:
        print('no files found')
    else:
        print(counter,'files found')
        #print(FileList)
        return (FileList, counter)

def lenopenreadlines(filename):
    #return number of line in a file
    with open(filename) as f:
        return len(f.readlines())


def main():
    """
    Main program entry.
    This program searches a directory and subdirectories to find a txt file.
    If in the same directory there is an fio file then that directory is
    valid.  The csv files in that directory can be processed only if there is no
    config file.  If config file exists, the process in incomplete and we wake up
    every 2 seconds to see if the config is gone.
    If there is no fio file in that directory, the directory can be ignored.
    """
    print ('hello')

    # The top argument for walk.
    topdir = '.'

    # The arg argument for walk, and subsequently ext for step
    exten = '.csv'
    dirn = '.'

    # Start the walk
    #GetListOfFiles = [['dummyfile' for _ in range(1)] for _ in range(2)]
    (GetListOfFiles, counter) = recursively_find_ext(topdir, exten)
    #print(GetListOfFiles, counter)

    length = 0
    while (counter > 0 ):
        if ( GetListOfFiles[counter-1] != ' '):
            length = lenopenreadlines(GetListOfFiles[counter-1])
            #print('line=',length, "for", GetListOfFiles[counter-1] )
            counter -= 1;

            print('modifying ',GetListOfFiles[counter])
            f = open(GetListOfFiles[counter], "r")
            lines = f.readlines()
            #print(lines)
            f.close()

            f = open(GetListOfFiles[counter], "w")
            linecounter = 1
            for line in lines:
                if (linecounter < length):
                    f.write(line)
                    linecounter += 1
                    #print('l of ',line, 'lc',linecounter)
            f.close()


if __name__=='__main__':
    main()
