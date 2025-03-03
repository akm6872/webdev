from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

class NoteCreate(BaseModel):
    title: str
    content: str
    owner_id: int

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
