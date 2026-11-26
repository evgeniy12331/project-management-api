
from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime,
    ForeignKey,
    func,
    CheckConstraint
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Task(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    __table_args__ = (
        CheckConstraint(
            "status IN ('todo', 'in_progress', 'done')",
            name="ck_tasks_status",
        ),
        CheckConstraint(
            "priority IN ('low', 'medium', 'high', 'urgent')",
            name="ck_tasks_priority",
        ),
    )



    project_id: Mapped[int] = mapped_column(
        ForeignKey("project.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    created_by_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="RESTRICT"),
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
        nullable=False,
        index=True
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        default="medium",
        nullable=False
    )

    due_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
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

    project: Mapped['user'] = relationship(
        back_populates='created_task',
        foreign_keys=[created_by_id]
        )

    subtasks: Mapped[list['subtask']] = relationship(
        back_populates='task',
        foreign_keys='subtask.task_id',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    assignees: Mapped[list['comment']] = relationship(
        back_populates='task',
        foreign_keys='taskAssignee.task_id',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    comments: Mapped[list['comment']] = relationship(
        back_populates='task',
        foreign_keys='comment.task_id',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    change_history: Mapped[list['change_history']] = relationship(
        back_populates='task',
        foreign_keys='change_history.task_id',
        cascade='all, delete-orphan',
        passive_deletes=True
    )