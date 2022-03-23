from loguru import logger
import pyrebase


config = {
    "apiKey": "AIzaSyCWzoiHMcL-waMA-RfPwoA6IOXSy1jE8Uw",
    "authDomain": "breakpoint-3d4ff.firebaseapp.com",
    "projectId": "breakpoint-3d4ff",
    "storageBucket": "breakpoint-3d4ff.appspot.com",
    "messagingSenderId": "287379710593",
    "appId": "1:287379710593:web:c5b6053158c0530bb9e380",
    "databaseURL": ""
}

email = "chinmay@simplified.co"
password = "test123"


try:
    firebase = pyrebase.initialize_app(config)
    firebase_auth = firebase.auth()
    # user = firebase_auth.sign_in_with_email_and_password(email, password)
    db = firebase.database()
except Exception as e:
    logger.debug(f"Error Initialising Firebase Connection: {e}")
