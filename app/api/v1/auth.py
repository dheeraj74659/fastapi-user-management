from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.db.database import get_db
from app.db.models.user import User
from app.services.auth import verify_password
from app.services.token import create_access_token, get_current_user

router = APIRouter()

@router.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    """Authenticate user and return JWT token."""
    async with db as session:
        result = await session.execute(select(User).filter(User.email == form_data.username))
        user = result.scalars().first()

        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        access_token = create_access_token({"sub": user.email}, timedelta(minutes=60))
        return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me/")
async def get_me(email: str = Depends(get_current_user)):
    """Get the current logged-in user's email."""
    return {"email": email}
