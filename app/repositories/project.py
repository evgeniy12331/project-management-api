from threading import settrace_all_threads

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project import Project

class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, proj_id: int):
        res = await self.session.execute(select(Project).where(Project.id == proj_id))
        return res.scalar_one_or_none()

    async def get_all(self, owner_id: int, limit: int = 20, offset: int = 0):
        res = await self.session.execute(select(Project).where(Project.owner_id == owner_id)
                                         .order_by(Project.id).limit(limit).offset(offset))
        return list(res.scalars().all())

    async def create(self, project: Project):
        self.session.add(project)
        await self.session.flush()
        await self.session.refresh(project)
        return project

    async def update(self, project: Project, data: dict):
        for field, value in data.items():
            setattr(project, field, value)
        await self.session.flush()
        await self.session.refresh(project)
        return project

    async def delete(self, project: Project):
        await self.session.delete(project)
        await self.session.flush()



