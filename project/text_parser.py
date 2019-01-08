class TextParser:
    def __init__(self):
        import os,sys

    def read_file(self, filename):
        file_reader = open(filename)
        file_text=file_reader.read()
        file_reader.close()
        return file_text
