from typing import Annotated

from pydantic import BaseModel,Field

class NotesCreate(BaseModel):

    title: Annotated[str, Field(min_length=4)]
    content: Annotated[str, Field(max_length=100)]
    is_done: Annotated[bool, Field(default=False)]