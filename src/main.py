import os
import uuid
from loguru import logger

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

# Ping API


@app.get("/ping")
async def ping():
    return "OK", 200


# Upload File API


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
    file_location = f"uploads/{file_name}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
        logger.info(f"Uploaded file saved at {file_location}")
    return {"success": True, "file": file_name}


# Get Upload File API
@app.get("/uploads/{file_id}")
async def read_item(file_id):
    file_location = f"uploads/{file_id}"
    if os.path.exists(file_location):
        return FileResponse(file_location)
    else:
        raise HTTPException(status_code=404, detail="File not found")


# Uploads Dirs
if not os.path.exists("uploads"):
    os.mkdir("uploads")
