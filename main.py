from fastapi import FastAPI
from router import notes

app = FastAPI()

app.include_router(notes)
