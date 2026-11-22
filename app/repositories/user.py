from threading import settrace_all_threads

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, user_id: int):
        res = await self.session.execute(select(User).where(User.id == user_id))
        return res.scalar_one_or_none()

    async def get_by_email(self, email: str):
        res = await self.session.execute(select(User).where(User.email == email))
        return res.scalar_one_or_none()

    async def get_username(self, username: str):
        res = await self.session.execute(select(User).where(User.username == username))
        return res.scalar_one_or_none()

    async def get_all(self, limit: int = 20, offset: int = 0):
        res = await self.session.execute(select(User).order_by(User.id).limit(limit).offset(offset))
        return list(res.scalars().all())

    async def create(self, user: User):
        self.session.add(user)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def update(self, user: User, data: dict):
        for field, value in data.items():
            setattr(user, field, value)
        await self.session.flush()
        await self.session.refresh(user)
        return user

    async def delete(self, user: User):
        await self.session.delete(user)
        await self.session.flush()

