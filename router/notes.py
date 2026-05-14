from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.schemas import NotesCreate,NoteResponse
from models.db_models import Notes
from database import get_db

router = APIRouter(prefix="/notes", tags=["notes"])

DBSession = Annotated[Session, Depends(get_db)]

@router.post("/", response_model=NoteResponse)
def create_notes(note: NotesCreate, db: DBSession):

    new_note = Notes(title=note.title,
                     content=note.content,
                     is_done=note.is_done)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/", response_model=list[NoteResponse])
def get_notes(db: DBSession):

    notes = db.query(Notes).all()
    return notes