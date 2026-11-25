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

## 2026-11-25: Decision: changes after supervisor meeting
- What: Matt confirmed the problem is Student-Project Allocation with project and supervisor capacities. Supervisors rank projects, not students. The goal is a stable matching. Ties are left out of the first version. The TP1 report is the literature review, and the website only needs basic working features.
- Alternatives considered: supervisors ranking students
- Why: Matt said supervisors rank projects, not students, so the supervisor ranking table is no longer part of the core design. The algorithm becomes the version where lecturers have preferences over projects, which is the case studied by Manlove and O'Malley. Ranking students will only be a possible later extension, for students a supervisor has already discussed a project with. Leaving out ties keeps the first version small enough to finish and test.
- Report section it feeds: Design

## 2026-11-25: Decision: supervisor ranking stored on Project, and R10 made a Must
- What: removed the SupervisorRanking table and added supervisor_rank to Project, with a rule that one supervisor cannot give two projects the same rank (UNIQUE supervisor, rank). Reworded R8 to "A supervisor can rank their own projects" and made it a Must. Made R10 (deadlines) a Must.
- Alternatives considered: keeping SupervisorRanking as a separate table; keeping R10 as a Should and dropping "until the deadline" from R3
- Why: a supervisor now ranks their own projects, so each project has one position in one supervisor's list and a column on Project is enough. The database can check the rule, as it does for the other rankings. R8 is a Must because the algorithm needs preferences from both sides. R3 says students can edit their ranking until the deadline, so the deadline feature has to exist and R10 cannot matter less than R3.
- Known limit: supervisor_rank belongs to the project, not to a round, so the same ranking applies in every round. This is fine for version 1.
- Report section it feeds: Design

## 2026-11-25: Decision: algorithm based on Manlove and O'Malley (2008)
- What: will implement spa-p-approx, their algorithm for the case where lecturers rank projects, as the main matching algorithm in backend/matching, with a stability checker that tests both blocking pairs and coalitions.
- Alternatives considered: the earlier Gale-Shapley version where lecturers rank students (Abraham, Irving and Manlove 2003); inventing my own method
- Why: Matt said supervisors rank projects, not students, so the version where lecturers rank students does not fit. The paper defines stability for exactly this case: no blocking pair, and no coalition (a group of students who could swap projects and all do better). Their algorithm finds a stable matching in linear time. Stable matchings can differ in size and finding the largest is NP-hard, so theirs is only guaranteed to be within a factor of 2 of the best. I will measure how many students get a place, compare against random and first-come-first-served baselines, and not claim the maximum.
- Tie-break: the algorithm leaves two choices arbitrary, the order students apply in and which student a lecturer drops when over capacity. My plan is a random order of students with a fixed seed, so results can be repeated. Not agreed with Matt yet.
- Report section it feeds: Background / Design

## 2026-11-25: Decision: keep Word files out of the repository
- What: added *.docx to .gitignore after committing my project definition by accident. Removed it before pushing.
- Alternatives considered: leaving it in the repository
- Why: the repository is public and the file may hold personal details. Documents stay on my laptop instead.
- Report section it feeds: none

## 2026-11-25: Questions for Matt
- Is a random order of students with a fixed seed an acceptable tie-break?
- What is the TP1 report deadline: 11 December, or a January date? The page says 18 January 2026, which looks like a typo.
- Do I need a separate Project Plan document?
