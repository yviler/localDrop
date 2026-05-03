import os

def createBreadcrumbs(directory:str) -> list:
    availablePaths = []
    currentPath = directory
    while(bool(currentPath)):
        availablePaths.append(currentPath)
        currentPath = os.path.split(currentPath)[0]
    return availablePaths