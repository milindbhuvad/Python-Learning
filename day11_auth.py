
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

router = APIRouter()
password_hash = PasswordHash.recommended()
security = HTTPBearer()

# Generate a strong secret key for your own project.
# Keep it private and load it from an environment variable.
SECRET_KEY = "3s1F-SgpIzybmRuaZVdDFaQiEjHk-Iy5UNqeH5Q3Cpo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Demo user only. In a real project, retrieve this from MySQL.
demo_user = {
    "email": "admin@example.com",
    "hashed_password": password_hash.hash("Admin@123")
}


class LoginRequest(BaseModel):
    email: str
    password: str


def create_access_token(email: str):
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": email,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


@router.post("/login")
def login(user: LoginRequest):

    if user.email != demo_user["email"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not password_hash.verify(
        user.password,
        demo_user["hashed_password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(user.email)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        if email != demo_user["email"]:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return email

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


@router.get("/profile")
def profile(current_user: str = Depends(get_current_user)):

    return {
        "message": "Authentication successful",
        "email": current_user
    }
