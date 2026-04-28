import os
from app.models.models import Item

def createItemObj(items:list,current_dir:str)-> list:
    objList = []
    for item in items:
        full_item = os.path.join(current_dir,item)
        stats = os.stat(full_item)
        objList.append(Item(
            filename=item,
            filesize=stats.st_size,
            filetype=os.path.splitext(item)[1],
            location=current_dir,
            isDirectory=os.path.isdir(full_item)
        ))
    return objList