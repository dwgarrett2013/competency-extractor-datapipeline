class TextParser:
    def __init__(self):
        import os,sys

    def read_file(self, filename):
        filehandle = open(filename)
        print(filehandle.read())
        filehandle.close()
