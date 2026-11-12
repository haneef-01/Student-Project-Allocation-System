# Requirements
- M = Must Have
- S = Should Have

##Student
-R1 (M) A student can log in securely and see only their own data. 
-R2 (M) A student can browse and search available projects.
-R3 (M) A student can rank the projects they find acceptable in order, and edit the ranking until the deadline. 
-R4 (S) A student can see their result with a plain-English explanation of why they got it. 

##Supervisor
-R5 (M) A supervisor can add and edit projects, including a capacity for each project.
-R6 (M) A supervisor can set a total supervision capacity across all their projects.
-R7 (S) A supervisor can see which students ranked their projects.
-R8 (S) A supervisor can submit their own rankings. 

##Admin
-R9 (M) An admin can bulk-import students, supervisors and projects from a file. 
-R10 (S) An admin can set deadlines and open or close preference submission.
-R11 (M) An admin can run the allocation for 500+ students and projects, and see who is left unallocated. 
-R12 (M) An admin can see how many students got their 1st, 2nd or 3rd choice. 
-R13 (S) An admin can export the results.

##Whole system
-R14 (M) A first-time user from a non-technical department can complete their task without training. You’d measure this in user testing with non-CS people. 
-R15 (M) The matching algorithm is a separate, replaceable module, tested on small hand-checked examples, and each result is checked for stability. 
