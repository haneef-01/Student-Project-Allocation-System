# Project Log

## 2026-10-27: Decision: how I record my project
- What: keep running notes instead of writing report chapters as I go
- Alternatives considered: writing chapters as I build
- Why: this is done to avoid forgetting what has been done in the software and updating what has been done in the report.
- so we take as much notes as possible so that when writing the report we are updated and never forget what we have done.
- the software may change as I build it, so a finished chapter could end up describing something I no longer do. Short notes are easy to update, and I turn them into the report at the end.
- Report section it feeds: Introduction / Method

## 2026-11-4: Decision: Structure of Repository
- What: Seperated backend/matching (pure python) from backend/app (web code)
- Alternatives considered: one backend folder with everything together
- Why: keeping the matching algorithm separate from the web code means I can test it on small examples I check by hand, swap in other algorithms to compare in my evaluation, and keep the web layer simple.
- Report section it feeds: Design

## 2026-11-12: Decision: domain model
- What: designed the domain model with User, Project, AllocationRound, Preference, SupervisorRanking, AllocationRun and Allocation
- Alternatives considered: storing rankings as columns on the student table; storing the algorithm on each allocation
- Why: Preference is its own table because a student ranks many projects and a project is ranked by many students, so each ranking is one row. The algorithm is recorded on the run so it is stored once and I can compare algorithms on the same round. Ties are left out of the first version to keep it simple.
- Report section it feeds: Design

## 2026-11-12: Decision: database tools
- What: wrote the User and Project models with SQLAlchemy, using SQLite for development
- Alternatives considered: writing raw SQL by hand; using Django; using MySQL
- Why: SQLite needs no setup and SQLAlchemy lets me move to PostgreSQL or MySQL later by changing one setting. Flask handles the web side and SQLAlchemy the data side, which keeps the layers separate.
- Report section it feeds: Design / Implementation

## 2026-11-12: Decision: database rules
- What: added the remaining five tables and made the database itself enforce the key rules:
  - a student cannot rank the same project twice in a round (UNIQUE round, student, project)
  - a student cannot give two projects the same rank in a round (UNIQUE round, student, rank)
  - ranks start at 1 and project capacity is at least 1 (CHECK constraints)
  - each email is used by one user only (UNIQUE email)
  - a student has at most one allocation per run (UNIQUE run, student)
  - every link between tables must point to a real row (foreign keys)
- Alternatives considered: checking the rules only in the Python code
- Why: if the Python code has a bug, the database still refuses bad data such as a duplicate ranking, so the matching algorithm can trust its input. The rules are also written in one place, which makes them easy to explain and to test.
- Known limits, to handle in the API: the database does not check that student_id belongs to a user with the role "student", that a supervisor's total capacity is respected, or that projects with rankings are deactivated instead of deleted. SQLite also needs foreign keys switched on in the app setup.
- Report section it feeds: Design / Implementation
