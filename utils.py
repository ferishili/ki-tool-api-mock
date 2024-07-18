from fastapi import HTTPException, Header, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import Optional
import os
from dotenv import load_dotenv
import logging

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
API_KEY = os.getenv("API_KEY")

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

oauth2_scheme = HTTPBearer()


def verify_token(token: str):
    credentials_exception = HTTPException(
        status_code=403, detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logging.debug(f"Decoded payload: {payload}")
        username: str = payload.get("sub")
        if username is None:
            logging.error(f"Token validation failed: Username is None")
            raise credentials_exception
        logging.debug(f"Token validation successful for user: {username}")
        return payload
    except JWTError as e:
        logging.error(f"JWT validation error: {e}")
        raise credentials_exception


def verify_api_key(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=403, detail="Missing API Key")
    token = authorization.split(" ")[1]
    if token != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
