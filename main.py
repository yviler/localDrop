from fastapi import FastAPI, Request, UploadFile, HTTPException, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
import shutil
from pathlib import Path
from utils.file import createItemObj
from utils.directories import createBreadcrumbs

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./ExampleRoot")
os.makedirs(UPLOAD_DIR, exist_ok=True)

BASE_DIR = Path(UPLOAD_DIR).resolve()

@app.get("/")
def index():
    return RedirectResponse("/dashboard")

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request, 
        "dashboard.html",
        {
            "base_dir": UPLOAD_DIR
        },
        )

@app.get("/upload")
def upload(request: Request):
    return templates.TemplateResponse(request, "upload.html")

@app.post("/upload")
async def upload(request: Request, file: UploadFile, directory:str = Form(""), name:str = Form("")):
    # UPLOADING SHOULD BECOME A STRING, SO CANT UPLOAD A DIRECTORY NAME WHICH COULD BE MISINTERPRETED
    
    if(bool(directory)):
        uploadPath = (Path(BASE_DIR) / directory).resolve()
    else:
        uploadPath = BASE_DIR 
        
    if(str(uploadPath).startswith(str(BASE_DIR)) != True):
        return templates.TemplateResponse(
            request, 
            "error.html",
            {
            "wrongPath": uploadPath,       
            },
        )
        
    if(bool(name)):
        extension = os.path.splitext(file.filename)[-1]
        filename = name + extension
    else:
        filename = file.filename
    file_path = os.path.join(uploadPath, filename)
    try:
        with open(file_path, "wb") as buffer:
            # if file name already exists, add (+=1), per existing, currently, it just doesnt upload  
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {e}")
    finally:
        await file.close()

    return templates.TemplateResponse(request, "success.html")

@app.get("/browse/{current_directory:path}")
def browse(current_directory: str, request: Request):
    absolutePath = Path(current_directory).resolve()
    items = os.listdir(absolutePath)
    itemList = createItemObj(items, absolutePath)
    
    # if we go back and forth via the browser, it doesnt activate this function
    directoryList = createBreadcrumbs(current_directory)
    
    if(str(absolutePath).startswith(str(BASE_DIR)) != True):
        return templates.TemplateResponse(
            request, 
            "error.html",
            {
            "wrongPath": current_directory,       
            },
        )
    
    directory = {
        "name": current_directory,
        "paths": directoryList
    }
    
    return templates.TemplateResponse(
            request,
            "browse.html",
            {
                "directory": directory,
                "items": itemList,
            },
        )
