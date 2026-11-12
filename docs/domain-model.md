# Domain Model

## Entities

### User
- Purpose: anyone who logs in. The role decides which portal they see.
- Fields: id, name, email, password_hash, role (student | supervisor | admin), department, max_students (supervisors only)

### Project
- Purpose: a project offered by one supervisor that students can rank.
- Fields: id, title, description, supervisor_id, capacity, department, is_active

### AllocationRound
- Purpose: one allocation cycle, with a deadline and a status.
- Fields: id, name, deadline, status (draft | open | closed | allocated), final_run_id

### Preference
- Purpose: one student's ranking of one project in one round.
- Fields: id, round_id, student_id, project_id, rank

### SupervisorRanking (to confirm with Matt)
- Purpose: a supervisor's ranking of one student in one round.
- Fields: id, round_id, supervisor_id, student_id, rank

### AllocationRun
- Purpose: one execution of one algorithm on one round, so algorithms can be compared.
- Fields: id, round_id, algorithm, run_at, summary (counts of 1st, 2nd, 3rd choice and unallocated)

### Allocation
- Purpose: the result for one student in one run.
- Fields: id, run_id, student_id, project_id
- An unallocated student simply has no row.

## Relationships
- One supervisor has many projects.
- One round has many preferences, supervisor rankings and runs.
- One student has many preferences, one per ranked project.
- One run has many allocations, at most one per student.

## Rules the database must enforce
- A student cannot rank the same project twice in a round.
- A student cannot give two projects the same rank in a round (strict preferences).
- Project capacity is at least 1.
- A supervisor's total capacity can be lower than the sum of their projects' capacities. That is the point of SPA.
- Projects with preferences or allocations are deactivated, never deleted.

## Decisions
- Single User table with a role, rather than separate tables: simpler login and role checks.
- Department is kept on User and Project, because the title promises multi-department use.
- Algorithm recorded on AllocationRun, not Allocation, so it is stored once.
- Ties are not supported in the first version.

## To confirm
- Do supervisors rank students or projects? This decides whether SupervisorRanking is needed and what it holds.
- Must students rank a minimum number of projects?
- Should ties be added later?
