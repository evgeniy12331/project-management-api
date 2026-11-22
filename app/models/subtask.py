
from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Subtask(Base):
    __tablename__ = "subtasks"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="todo",
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
