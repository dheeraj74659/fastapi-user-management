from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: constr(min_length=8, max_length=128)

class UserResponse(UserBase):
    id: int
    role: str

    class Config:
        from_attributes = True