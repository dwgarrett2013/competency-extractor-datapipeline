from project.text_parser import TextParser
import sys
import os

if(len(sys.argv)!=2):
    print("Filename is a required input.  Please provide one.")
else:
    parser=TextParser()
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    print(fileDir)

    # For accessing the file in the same folder
    filename = sys.argv[1]
    print(filename)
    #parser.readFile(filename)

    # For accessing the file in a folder contained in the current folder
    filePath = os.path.join(fileDir,"project",filename)
    print(filePath)
    parser.read_file(filePath)

    # For accessing the file in the parent folder of the current folder
    #filename = os.path.join(fileDir, '../same.txt')
    #readFile(filename)

    # For accessing the file inside a sibling folder.
    #filename = os.path.join(fileDir, '../Folder2/same.txt')
    #filename = os.path.abspath(os.path.realpath(filename))
    #print(filename)
    #parser.readFile(filename)



