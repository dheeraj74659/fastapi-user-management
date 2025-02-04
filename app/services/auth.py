from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from app.services.token import get_current_user
from app.db.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.user import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

def hash_password(password: str) -> str:
    """Hash a plain text password using bcrypt."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """verify a plain text password against the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)



async def get_user_from_db(email: str, db: AsyncSession):
    async with db as session:
        result = await session.execute(select(User).filter(User.email == email))
        return result.scalars().first()

async def get_current_active_user(email: str = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    """Retrieve the current logged-in user from the database."""
    user = await get_user_from_db(email, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

async def is_admin(user: User = Depends(get_current_active_user)):
    """Check if the user has admin role."""
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return user
