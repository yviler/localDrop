import os

def createBreadcrumbs(directory:str) -> list:
    availablePaths = []
    currentPath = directory
    while(bool(currentPath)):
        availablePaths.append(currentPath)
        currentPath = os.path.split(directory)[0]
    print(availablePaths)