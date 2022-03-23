import importlib
from tkinter import E
from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import BaseModel
from firebase_db.firebase_connection import firebase_auth


router = APIRouter()


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/break_point/users/login/auth", tags=["Users"])
def list_users(user_login: UserLogin):
    try:
        # Get All the Users from Child: USer
        aut_status = firebase_auth.sign_in_with_email_and_password(
            user_login.email, user_login.password)

        print(aut_status)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"Error Listing Users: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error Listing Users: {e}")


@router.get("/accounts/google/login/callback", tags=["Users"])
def signup_users(data):
    try:
        print("pass")
    except Exception as e:
        logger.debug("Error in User Signin with Google")
