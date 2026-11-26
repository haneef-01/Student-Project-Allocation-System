def spa_p_approx(instance, order):
    """Find a stable matching for SPA-P (Manlove and O'Malley, 2008).

    instance: a dict like FIGURE_1 in examples.py
    order: list of students, the order they apply in
    Returns a dict of student -> project.
    """
    # Copies, because the algorithm deletes projects from students list
    student_prefs = {s: list(p) for s, p in instance["student_prefs"].items()}
    project_capacity = instance["project_capacity"]
    project_lecturer = instance["project_lecturer"]
    lecturer_capacity = instance["lecturer_capacity"]
    lecturer_prefs = instance["lecturer_prefs"]

    # Position of each project in its lecturer's list. 0 is best.
    lecturer_rank = {
        l: {p: i for i, p in enumerate(projects)}
        for l, projects in lecturer_prefs.items()
    }

    assigned = {}  # student -> project

    def students_on(project):
        return [s for s, p in assigned.items() if p == project]

    def students_with(lecturer):
        return [s for s, p in assigned.items() if project_lecturer[p] == lecturer]

    def worst_nonempty(lecturer):
        used = [p for p in lecturer_prefs[lecturer] if students_on(p)]
        if not used:
            return None
        return max(used, key=lambda p: lecturer_rank[lecturer][p])

    while True:
        # Rule 1: next student who has no project yet and still has projects to try
        waiting = [s for s in order if s not in assigned and student_prefs[s]]
        if not waiting:
            break
        student = waiting[0]
        project = student_prefs[student][0]
        lecturer = project_lecturer[project]

        # Rule 2: the project is full, so reject and cross it off their list
        if len(students_on(project)) >= project_capacity[project]:
            student_prefs[student].remove(project)

        # Rule 3: the lecturer is full and this is their worst non-empty project
        elif (len(students_with(lecturer)) >= lecturer_capacity[lecturer]
              and worst_nonempty(lecturer) == project):
            student_prefs[student].remove(project)

        # Otherwise: assign the student to the project for now
    
        else:
            assigned[student] = project

            # Rule 4: the lecturer is now over capacity, so drop one student
            # from the lecturer's worst non-empty project
            if len(students_with(lecturer)) > lecturer_capacity[lecturer]:
                worst = worst_nonempty(lecturer)
                dropped = students_on(worst)[-1]
                del assigned[dropped]
                student_prefs[dropped].remove(worst)

            # Rule 5: the lecturer is full, so delete every project they rank
            # below their worst non-empty one from all students' lists
            if len(students_with(lecturer)) == lecturer_capacity[lecturer]:
                worst = worst_nonempty(lecturer)
                for p in lecturer_prefs[lecturer]:
                    if lecturer_rank[lecturer][p] > lecturer_rank[lecturer][worst]:
                        for prefs in student_prefs.values():
                            if p in prefs:
                                prefs.remove(p)

    return assigned