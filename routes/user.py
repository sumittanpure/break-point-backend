from cmath import log
import imp
import importlib
from tkinter import E
from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import BaseModel
from firebase_db.firebase_connection import cred
from firebase_admin import auth, initialize_app

router = APIRouter()


@router.get("/break_point/users/login/auth", tags=["Users"])
def list_users(login_token: str):
    try:
        # Get All the Users from Child: USer
        # print(login_token)
        # firebase_app = initialize_app(cred)
        token_ver_res = auth.verify_id_token(login_token)
        print(token_ver_res)
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"Error Listing Users: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error Listing Users: {e}")
