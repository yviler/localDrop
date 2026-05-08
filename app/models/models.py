class Item:
    def __init__(self, filename:str, fullname:str, filesize:int, filetype:str, location:str, isDirectory:bool, relativePath:str):
        self.filename = filename
        self.fullname = fullname
        self.filesize = filesize
        self.filetype = filetype
        self.location = location
        self.isDirectory = isDirectory
        self.relativePath = relativePath
    
    def __repr__(self):
        return f"Item(filename={self.filename!r}, fullname={self.fullname}, filesize={self.filesize}, filetype={self.filetype!r}, location={self.location!r}, isDirectory={self.isDirectory!r}, relativePath={self.relativePath})"