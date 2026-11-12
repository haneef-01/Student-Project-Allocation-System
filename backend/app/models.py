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

class AllocationRound(Base):
    __tablename__ = "allocation_rounds"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    deadline: Mapped[Optional[datetime]] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20), default="draft")  # draft | open | closed | allocated


class Preference(Base):
    __tablename__ = "preferences"
    __table_args__ = (
        UniqueConstraint("round_id", "student_id", "project_id"),  # no ranking a project twice
        UniqueConstraint("round_id", "student_id", "rank"),        # no two projects with the same rank
        CheckConstraint("rank >= 1"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    round_id: Mapped[int] = mapped_column(ForeignKey("allocation_rounds.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    rank: Mapped[int]


class SupervisorRanking(Base):  # to confirm with Matt
    __tablename__ = "supervisor_rankings"
    __table_args__ = (
        UniqueConstraint("round_id", "supervisor_id", "student_id"),
        UniqueConstraint("round_id", "supervisor_id", "rank"),
        CheckConstraint("rank >= 1"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    round_id: Mapped[int] = mapped_column(ForeignKey("allocation_rounds.id"))
    supervisor_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    rank: Mapped[int]


class AllocationRun(Base):
    __tablename__ = "allocation_runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    round_id: Mapped[int] = mapped_column(ForeignKey("allocation_rounds.id"))
    algorithm: Mapped[str] = mapped_column(String(50))
    run_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    is_final: Mapped[bool] = mapped_column(default=False)
    summary: Mapped[Optional[dict]] = mapped_column(JSON)  # counts of 1st, 2nd, 3rd choice, unallocated


class Allocation(Base):
    __tablename__ = "allocations"
    __table_args__ = (UniqueConstraint("run_id", "student_id"),)  # one project per student per run

    id: Mapped[int] = mapped_column(primary_key=True)
    run_id: Mapped[int] = mapped_column(ForeignKey("allocation_runs.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
