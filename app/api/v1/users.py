from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.database import get_db
from app.db.models.user import User
from app.db.schemas.user import UserCreate, UserResponse
from app.services.auth import hash_password , is_admin

router = APIRouter()    

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(User).filter(User.email == user.email))
        existing_user = result.scalars().first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        new_user = User(
            username=user.username,
            email=user.email,
            hashed_password=hash_password(user.password),
            role="user"
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


@router.get("/users/", response_model=list[UserResponse], dependencies=[Depends(is_admin)])
async def get_users(db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(User))
        users = result.scalars().all()  # Fetch all users
        if not users:
            raise HTTPException(status_code=404, detail="No users found")
        return users


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    async with db as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

@router.delete("/users/{user_id}/", dependencies=[Depends(is_admin)])
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Delete a user (Admin only)."""
    async with db as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        await session.delete(user)
        await session.commit()
        return {"message": "User deleted successfully"}
