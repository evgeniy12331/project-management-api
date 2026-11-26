
from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Project(Base):
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="active",
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    owner: Mapped['user'] = relationship(
        back_populates='owned_project',
        foreign_keys=[owner_id]
    )
    tasks: Mapped[list['task']] = relationship(
        back_populates='project',
        foreign_keys='task.project_id',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    members: Mapped[list['project_member']] = relationship(
        back_populates='project',
        foreign_keys='project_member.project_id',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
