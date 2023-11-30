import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Your secret key (keep it secure)
SECRET_KEY = "My_Sectret_3w4r5t"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_jwt_token(UserName: str):
    expiration_time = datetime.utcnow() + timedelta(days=60)
    payload = {"sub": UserName, "exp": expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials some error occured",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        UserName: str = payload.get("sub")
        if UserName is None:
            raise credentials_exception
        return UserName
    except Exception as e:
        raise credentials_exception