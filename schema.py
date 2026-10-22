from pydantic import BaseModel


class BaseStudent(BaseModel):
    roll: str
    first_name: str
    last_name: str
    session: int
    department: str

class StudentCreateRequet(BaseStudent):
    pass

class StudentUpdateRequest(BaseModel):
    first_name: str
    last_name: str
    department: str

class StudentResponse(BaseStudent):
    id : int

    class Config:
        orm_mode = True 