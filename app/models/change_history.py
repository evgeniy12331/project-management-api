
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


class ChangeHistory(Base):
    __tablename__ = "change_history"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    changed_by_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True
    )

    field_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    old_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    new_value: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
