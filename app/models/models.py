class Item:
    def __init__(self, filename:str, filesize:int, filetype:str, location:str, isDirectory:bool):
        self.filename = filename
        self.filesize = filesize
        self.filetype = filetype
        self.location = location
        self.isDirectory = isDirectory
    
    def __repr__(self):
        return f"Item(filename={self.filename!r}, filesize={self.filesize}, filetype={self.filetype!r}, location={self.location!r}, isDirectory={self.isDirectory})"