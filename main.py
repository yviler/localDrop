from fastapi import FastAPI, Request, UploadFile, HTTPException, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
import os
import shutil
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "/home/boba/Desktop/FileExample"
os.makedirs(UPLOAD_DIR, exist_ok=True)

BASE_DIR = Path(UPLOAD_DIR).resolve()

@app.get("/")
def index():
    return RedirectResponse("/dashboard")

@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/upload")
def upload(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

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

    #change to better UI 
    return {"Filename": file.filename, "Message": "File uploaded succefully to"}

@app.get("/browse/{current_directory}")
def browse(current_directory: str, request: Request):
    
   directory = {
       "name": current_directory
   }
   return templates.TemplateResponse("browse.html", 
                                     {"request": request,
                                     "directory": directory},
                                     )