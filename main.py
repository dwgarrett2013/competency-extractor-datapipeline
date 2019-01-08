from project.text_parser import TextParser
from project.text_cleaner import TextCleaner
import sys
import os

if(len(sys.argv)!=2):
    print("Filename is a required input.  Please provide one.")
else:
    parser=TextParser()
    cleaner=TextCleaner()
    fileDir = os.path.dirname(os.path.realpath('__file__'))

    # For accessing the file in the same folder
    filename = sys.argv[1]

    # For accessing the file in a folder contained in the current folder
    filePath = os.path.join(fileDir,"project",filename)
    #print("Path to file: ",filePath)
    #print("\n")
    #print("File contents:")
    file_text=parser.read_file(filePath)
    print(cleaner.clean_file_text(file_text))






