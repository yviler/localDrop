import os

def createItemObj(items:list,current_dir:str)-> list:
    for item in items:
        full_item = os.path.join(current_dir,item)
        stats = os.stat(full_item)
        print(stats)
        break