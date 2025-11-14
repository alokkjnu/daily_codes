import os
import shutil
import uuid
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "uploads"

def ensure_upload_dir():
    """Create upload folder if not exists."""
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)

def save_upload_file(file: UploadFile) -> str:
    """Save the uploaded file securely and return the file path."""
    ensure_upload_dir()
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in [".pdf", ".docx"]:
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files are supported.")

    unique_filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return file_path

def cleanup_file(path: str):
    """Remove temporary file from disk."""
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass
