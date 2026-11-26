# Figure 1 from Manlove and O'Malley (2008).
# Rebuilt from the paper's text, so check it against the figure.
FIGURE_1 = {
    "student_prefs": {"s1": ["p1", "p2"], "s2": ["p1"]},
    "project_capacity": {"p1": 1, "p2": 1},
    "project_lecturer": {"p1": "l1", "p2": "l2"},
    "lecturer_capacity": {"l1": 1, "l2": 1},
    "lecturer_prefs": {"l1": ["p1"], "l2": ["p2"]},
}

THREE_STUDENTS = {
    "student_prefs": {"s1": ["p1", "p3"], "s2": ["p2", "p3"], "s3": ["p1"]},
    "project_capacity": {"p1": 1, "p2": 1, "p3": 1},
    "project_lecturer": {"p1": "l1", "p2": "l1", "p3": "l2"},
    "lecturer_capacity": {"l1": 1, "l2": 1},
    "lecturer_prefs": {"l1": ["p1", "p2"], "l2": ["p3"]},
}