from fastapi import APIRouter
from models.schemas import NotesCreate

router = APIRouter(prefix="/notes", tags=["notes"])

@router.post("/")
def create_notes(note: NotesCreate):
    ...
