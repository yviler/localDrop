from fastapi import FastAPI, Request, UploadFile, HTTPException, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
import shutil
from pathlib import Path
from utils.file import createItemObj

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
    return templates.TemplateResponse(request, "dashboard.html")

@app.get("/upload")
def upload(request: Request):
    return templates.TemplateResponse(request, "upload.html")

@app.post("/upload")
async def upload(request: Request, file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {e}")
    finally:
        await file.close()

    return templates.TemplateResponse(request, "success.html")

@app.get("/browse/{current_directory}")
#TODO: File should not be ABSOLUTE DIRECTORY, make it relative
def browse(current_directory: str, request: Request):
    #use Path.resolve(current_directory)
    #if not same with base_dir, output error 
    items = os.listdir(current_directory)
    itemList = createItemObj(items, current_directory)
    print(createItemObj(items, current_directory))
    
    directory = {
        "name": current_directory,
        "item_amount": len(items)
    }
    
    return templates.TemplateResponse(
            request,
            "browse.html",
            {
                "directory": directory,
                "items": itemList,
            },
        )
