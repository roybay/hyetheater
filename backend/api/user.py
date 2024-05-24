from fastapi import APIRouter, HTTPException, Depends
from pony.orm import db_session
from pydantic import BaseModel, EmailStr
from api.orm import User, connect_db
from api.utils import get_password_hash, verify_password, create_access_token, get_current_user, check_superadmin, validate_password_policy  # noqa E501
from datetime import timedelta

router = APIRouter()
connect_db()


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class MeName(BaseModel):
    email: str


class UserUpdate(BaseModel):
    email: EmailStr = None
    password: str = None


@router.post("/api/v1/users", tags=["user"], response_model=Token)
@db_session
def create_user(user: UserCreate):
    db_user = User.get(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    validate_password_policy(user.password)
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, password_hash=hashed_password)
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": new_user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/api/v1/token", tags=["user"], response_model=Token)
@db_session
def login(user: UserLogin):
    db_user = User.get(email=user.email)
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": db_user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/api/v1/users/me", tags=["user"], response_model=MeName)
def read_users_me(current_user: str = Depends(get_current_user)):
    return {"email": current_user}


@router.put("/api/v1/users/{user_id}", tags=["user"])
@db_session
def update_user(user_id: int, user_update: UserUpdate, current_user: User = Depends(check_superadmin)):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_update.email:
        user.email = user_update.email
    if user_update.password:
        validate_password_policy(user_update.password)
        user.password_hash = get_password_hash(user_update.password)
    return {"message": "User updated successfully"}


@router.delete("/api/v1/users/{user_id}", tags=["user"])
@db_session
def delete_user(user_id: int, current_user: User = Depends(check_superadmin)):
    user = User.get(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.delete()
    return {"message": "User deleted successfully"}
