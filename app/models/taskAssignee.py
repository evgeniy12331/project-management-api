
from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column,relationship

from app.models.base import Base


class TaskAssignee(Base):
    __tablename__ = "taskAssignee"

    __table_args__ = (
        UniqueConstraint(
            "task_id",
            "user_id",
            name="uq_task_assignee"
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    task_id: Mapped[int] = mapped_column(
        ForeignKey("task.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    assigned_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    task: Mapped['task'] = relationship(
        back_populates='assignees',
        foreign_keys=[task_id]
    )

    user: Mapped['user'] = relationship(
        back_populates='task_assignments',
        foreign_keys=[user_id]
    )
