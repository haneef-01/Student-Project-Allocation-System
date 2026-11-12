from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import (
    JSON,
    CheckConstraint,
    DateTime,
    ForeignKey,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20))  # student | supervisor | admin
    department: Mapped[Optional[str]] = mapped_column(String(100))
    max_students: Mapped[Optional[int]]  # supervisors only

    projects: Mapped[list["Project"]] = relationship(back_populates="supervisor")


class Project(Base):
    __tablename__ = "projects"
    __table_args__ = (CheckConstraint("capacity >= 1"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    description: Mapped[Optional[str]]
    supervisor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    capacity: Mapped[int] = mapped_column(default=1)
    department: Mapped[Optional[str]] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(default=True)

    supervisor: Mapped["User"] = relationship(back_populates="projects")

