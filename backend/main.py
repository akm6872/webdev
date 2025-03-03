from fastapi import FastAPI
from routes import user, note

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(note.router, prefix="/notes", tags=["Notes"])

@app.get("/")
def read_root():
    return {"message": "Lecture Notes API is running!"}
