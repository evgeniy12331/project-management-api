from datetime import datetime
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy import func
from sqlalchemy.orm import Mapped,mapped_column, relationship
from app.models.base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(100),
                                       unique=True,
                                       nullable=False,
                                       index=True)
    username: Mapped[str] = mapped_column(String(50),
                                          unique=True,
                                          nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(100),
                                                 nullable=False)
    role: Mapped[str] = mapped_column(String(50),
                                      default='member',
                                      nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean,
                                            default=True,
                                            nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                         server_default=func.now(),
                                                         nullable=False)
    update_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                server_default=func.now(),
                                                nullable=False)

    owned_project: Mapped[list['project']] = relationship(
        back_populates='owner',
        foreign_keys='project.owner.id'
    )
    project_members: Mapped[list['project_member']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
        passive_deletes=True
    )
    created_tasks = Mapped[list['task']] = relationship(
        back_populates='created_by',
        foreign_keys='task.created_by_id'
    )

    task_assignments = Mapped[list['taskAssignee']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
        passive_deletes=True
    )

    comments = Mapped[list['comment']] = relationship(
        back_populates='author',
        foreign_keys='comment.author_id'
    )






