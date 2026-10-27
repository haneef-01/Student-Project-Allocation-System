# Requirements
M = Must Have
S = Should Have

**Student**
(M) A student can log in securely and see only their own data. (Three-portal design)
(M) A student can browse and search available projects. (Definition form)
(M) A student can rank the projects they find acceptable in order, and edit the ranking until the deadline. (Stable matching needs ranked preference lists)
(S) A student can see their result with a plain-English explanation of why they got it. (Transparency, from originality section)

**Supervisor**
(M) A supervisor can add and edit projects, including a capacity for each project. (SPA puts capacity limits on projects and on lecturers.) 
(M) A supervisor can set a total supervision capacity across all their projects.
(S) A supervisor can see which students ranked their projects.
(S) A supervisor can submit their own rankings. 

**Admin**
(M) An admin can bulk-import students, supervisors and projects from a file. (Aston has 500+ projects, so entering them by hand isn’t realistic)
(S) An admin can set deadlines and open or close preference submission.
(M) An admin can run the allocation for 500+ students and projects, and see who is left unallocated. (Set your own target time)
(M) An admin can see how many students got their 1st, 2nd or 3rd choice. (Profile, meaning how many students get each rank of choice, is a standard way to judge an allocation. It also feeds your evaluation chapter.) 
(S) An admin can export the results.

**Whole system**
(M) A first-time user from a non-technical department can complete their task without training. You’d measure this in user testing with non-CS people. 
(M) The matching algorithm is a separate, replaceable module, tested on small hand-checked examples, and each result is checked for stability. (Gives you comparison and evaluation material)
