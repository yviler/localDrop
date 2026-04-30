import os
from app.models.models import Item
from os import path

def createItemObj(items:list,current_dir:str)-> list:
    objList = []
    for item in items:
        full_item = os.path.join(current_dir,item)
        stats = os.stat(full_item)
        objList.append(Item(
            filename=os.path.splitext(item)[0],
            filesize=normalizeFileSize(stats.st_size),
            filetype=os.path.splitext(item)[1][1:],
            location=current_dir,
            isDirectory=os.path.isdir(full_item),

        ))
    return objList

def normalizeFileSize(filesize:int)-> str:
    count = 0
    sizeDict = {
        0: "Bytes",
        1: "KB",
        2: "MB",
        3: "GB",
        4: "TB",
        5: "PB"
    }
    while(filesize>999):
        filesize/=1000
        count+=1
    filesize = str(round(filesize,2)) + " " + sizeDict.get(count)
    return filesize