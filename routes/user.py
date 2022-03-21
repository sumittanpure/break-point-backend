import importlib
from fastapi import APIRouter, HTTPException
from loguru import logger
from firebase_db.firebase_connection import db


router = APIRouter()


@router.get("/break_point/users/ls", tags=["Users"])
def list_users():
    try:
        # Get All the Users from Child: USer
        user = db.child("users").get()
        print(user.val())
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.debug(f"Error Listing Users: {e}")
        raise HTTPException(
            status_code=500, detail=f"Error Listing Users: {e}")
