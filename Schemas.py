from pydantic import BaseModel


class SignupModel(BaseModel):
    Name: str
    Email: str
    Age: int
    Username: str
    Password: str


class LoginModel(BaseModel):
    Username: str
    Password: str
