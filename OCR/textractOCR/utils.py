import shutil
from pathlib import Path
from fastapi import UploadFile 
from tempfile import NamedTemporaryFile

def save_upload_file_tmp(upload_file: UploadFile, dest: str):
    """Returns temporary path for uploaded file"""
    try:
        dest = Path(dest)
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path

