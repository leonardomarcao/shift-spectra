import os
import shutil
import tempfile
from typing import List

from app.crud import crud_shift
from app.db.session import sync_session
from app.tasks.import_shift import import_shift
from fastapi import APIRouter, File, UploadFile

api_router = APIRouter()
db = sync_session()


@api_router.post("/upload/")
async def upload_files(files: List[UploadFile] = File(...)):
    filenames = []
    temp_dir = tempfile.mkdtemp()
    try:
        for file in files:
            # Save file to disk
            file_location = os.path.join(temp_dir, file.filename)
            with open(file_location, "wb") as buffer:
                buffer.write(await file.read())

            import_shift(file_location)

            filenames.append(file.filename)
    except Exception as e:
        shutil.rmtree(temp_dir)
        raise e

    return {"filenames": filenames}


@api_router.get("/grouped-by-month/")
async def grouped_by_month():
    return crud_shift.get_group_by_month(db)


@api_router.get("/by-month/{year}/{month}")
async def by_month(year: int, month: int):
    return crud_shift.get_by_month_range(db, year, month)


@api_router.get("/graph/{year}/{month}/{day}")
async def shift_graph(year: int, month: int, day: int):
    return crud_shift.get_shift_graph(db, year, month, day)
