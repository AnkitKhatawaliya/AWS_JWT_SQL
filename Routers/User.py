from fastapi import APIRouter, Depends
from DataBASE.User_DB import Check_user, add_a_user
from HASH import Covert_to_HASH
from JWT.Create_JWT import create_jwt_token, get_current_user
from Schemas import SignupModel, LoginModel

router = APIRouter()


@router.post('/Signup')
def Signup(User: SignupModel):
    User.Password = Covert_to_HASH(User.Password)
    add_a_user(User)
    jwt_token = create_jwt_token(User.Username)
    return {"username":"Registered","JWT_TOKEN":jwt_token}


@router.post('/Login')
def Login(User: LoginModel):
    User.Password = Covert_to_HASH(User.Password)
    if Check_user(User):
        jwt_token = create_jwt_token(User.Username)
        return {"Login": "Succesfull","JWT_TOKEN":jwt_token}
    else:
        return {"Invalid":"Credentials"}

@router.get('/DATA')
def Data(current_user: str = Depends(get_current_user)):
    return {"DATA": current_user}