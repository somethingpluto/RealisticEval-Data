f
r
o
m
 
t
y
p
i
n
g
 
i
m
p
o
r
t
 
I
t
e
r
a
b
l
e
,
 
L
i
s
t






c
l
a
s
s
 
C
o
u
r
s
e
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
c
o
u
r
s
e
_
i
d
,
 
m
u
s
t
_
c
o
u
r
s
e
s
=
N
o
n
e
,
 
r
e
c
o
m
m
e
n
d
_
c
o
u
r
s
e
s
=
N
o
n
e
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
i
d
 
=
 
c
o
u
r
s
e
_
i
d


 
 
 
 
 
 
 
 
s
e
l
f
.
m
u
s
t
_
c
o
u
r
s
e
s
 
=
 
m
u
s
t
_
c
o
u
r
s
e
s
 
i
f
 
m
u
s
t
_
c
o
u
r
s
e
s
 
i
s
 
n
o
t
 
N
o
n
e
 
e
l
s
e
 
[
]


 
 
 
 
 
 
 
 
s
e
l
f
.
r
e
c
o
m
m
e
n
d
_
c
o
u
r
s
e
s
 
=
 
r
e
c
o
m
m
e
n
d
_
c
o
u
r
s
e
s
 
i
f
 
r
e
c
o
m
m
e
n
d
_
c
o
u
r
s
e
s
 
i
s
 
n
o
t
 
N
o
n
e
 
e
l
s
e
 
[
]






c
l
a
s
s
 
L
e
v
e
l
e
d
C
o
u
r
s
e
:


 
 
 
 
d
e
f
 
_
_
i
n
i
t
_
_
(
s
e
l
f
,
 
c
o
u
r
s
e
:
 
C
o
u
r
s
e
,
 
l
e
v
e
l
:
 
i
n
t
)
:


 
 
 
 
 
 
 
 
s
e
l
f
.
c
o
u
r
s
e
 
=
 
c
o
u
r
s
e


 
 
 
 
 
 
 
 
s
e
l
f
.
l
e
v
e
l
 
=
 
l
e
v
e
l




d
e
f
 
t
o
p
o
l
o
g
i
c
a
l
_
s
o
r
t
(
c
o
u
r
s
e
s
:
 
I
t
e
r
a
b
l
e
[
C
o
u
r
s
e
]
)
 
-
>
 
L
i
s
t
[
L
e
v
e
l
e
d
C
o
u
r
s
e
]
:


 
 
 
 
"
"
"


 
 
 
 
P
e
r
f
o
r
m
s
 
a
 
t
o
p
o
l
o
g
i
c
a
l
 
s
o
r
t
 
o
n
 
a
 
c
o
l
l
e
c
t
i
o
n
 
o
f
 
c
o
u
r
s
e
s
 
u
s
i
n
g
 
K
a
h
n
'
s
 
a
l
g
o
r
i
t
h
m
.




 
 
 
 
A
r
g
s
:


 
 
 
 
c
o
u
r
s
e
s
 
(
I
t
e
r
a
b
l
e
[
C
o
u
r
s
e
]
)
:
 
A
 
c
o
l
l
e
c
t
i
o
n
 
o
f
 
c
o
u
r
s
e
s
,
 
w
h
e
r
e
 
e
a
c
h
 
c
o
u
r
s
e
 
i
s
 
a
s
s
u
m
e
d
 
t
o
 
h
a
v
e
 
a
n
 
'
i
d
'
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
o
p
t
i
o
n
a
l
l
y
 
'
m
u
s
t
_
c
o
u
r
s
e
s
'
 
a
n
d
 
'
r
e
c
o
m
m
e
n
d
_
c
o
u
r
s
e
s
'
 
l
i
s
t
s
 
o
f
 
c
o
u
r
s
e
 
i
d
s
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
L
i
s
t
[
L
e
v
e
l
e
d
C
o
u
r
s
e
]
:
 
A
 
l
i
s
t
 
o
f
 
c
o
u
r
s
e
s
 
s
o
r
t
e
d
 
i
n
 
t
o
p
o
l
o
g
i
c
a
l
 
o
r
d
e
r
,
 
e
a
c
h
 
w
r
a
p
p
e
d
 
i
n
 
a
 
L
e
v
e
l
e
d
C
o
u
r
s
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
b
j
e
c
t
 
t
h
a
t
 
a
l
s
o
 
c
o
n
t
a
i
n
s
 
t
h
e
 
l
e
v
e
l
 
(
i
.
e
.
,
 
d
i
s
t
a
n
c
e
 
f
r
o
m
 
s
t
a
r
t
 
i
n
 
t
o
p
o
l
o
g
i
c
a
l
 
s
o
r
t
)
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
V
a
l
u
e
E
r
r
o
r
:
 
I
f
 
t
h
e
r
e
 
i
s
 
a
 
c
y
c
l
e
 
d
e
t
e
c
t
e
d
 
i
n
 
t
h
e
 
c
o
u
r
s
e
s
,
 
w
h
i
c
h
 
p
r
e
v
e
n
t
s
 
a
 
c
o
m
p
l
e
t
e
 
t
o
p
o
l
o
g
i
c
a
l
 
s
o
r
t
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s
,
 
w
h
e
r
e
 
t
h
e
 
k
e
y
 
i
s
 
t
h
e
 
c
o
u
r
s
e
 
i
d
 
a
n
d
 
t
h
e
 
v
a
l
u
e
 
i
s
 
a
 
C
o
u
r
s
e
 
o
b
j
e
c
t
.


 
 
 
 
c
o
u
r
s
e
_
d
i
c
t
 
=
 
{
c
o
u
r
s
e
.
i
d
:
 
c
o
u
r
s
e
 
f
o
r
 
c
o
u
r
s
e
 
i
n
 
c
o
u
r
s
e
s
}




 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s
,
 
w
h
e
r
e
 
t
h
e
 
k
e
y
 
i
s
 
t
h
e
 
c
o
u
r
s
e
 
i
d
 
a
n
d
 
t
h
e
 
v
a
l
u
e
 
i
s
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s


 
 
 
 
#
 
t
h
a
t
 
m
u
s
t
 
b
e
 
t
a
k
e
n
 
b
e
f
o
r
e
 
i
t
.


 
 
 
 
m
u
s
t
_
b
e
f
o
r
e
_
d
i
c
t
 
=
 
{
c
o
u
r
s
e
.
i
d
:
 
c
o
u
r
s
e
.
m
u
s
t
_
c
o
u
r
s
e
s
 
f
o
r
 
c
o
u
r
s
e
 
i
n
 
c
o
u
r
s
e
s
}




 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s
,
 
w
h
e
r
e
 
t
h
e
 
k
e
y
 
i
s
 
t
h
e
 
c
o
u
r
s
e
 
i
d
 
a
n
d
 
t
h
e
 
v
a
l
u
e
 
i
s
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s


 
 
 
 
#
 
t
h
a
t
 
c
a
n
 
b
e
 
t
a
k
e
n
 
a
f
t
e
r
 
i
t
.


 
 
 
 
r
e
c
o
m
m
e
n
d
_
a
f
t
e
r
_
d
i
c
t
 
=
 
{
c
o
u
r
s
e
.
i
d
:
 
c
o
u
r
s
e
.
r
e
c
o
m
m
e
n
d
_
c
o
u
r
s
e
s
 
f
o
r
 
c
o
u
r
s
e
 
i
n
 
c
o
u
r
s
e
s
}




 
 
 
 
#
 
C
r
e
a
t
e
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s
,
 
w
h
e
r
e
 
t
h
e
 
k
e
y
 
i
s
 
t
h
e
 
c
o
u
r
s
e
 
i
d
 
a
n
d
 
t
h
e
 
v
a
l
u
e
 
i
s
 
a
 
l
i
s
t
 
o
f
 
a
l
l
 
c
o
u
r
s
e
s


 
 
 
 
#
 
t
h
a
t
 
m
u
s
t
 
b
e
 
t
a
k
e
n
 
b
e
f
o
r
e
 
i
t
.
import unittest

class Course:
    def __init__(self, course_id, must_courses=None, recommend_courses=None):
        self.id = course_id
        self.must_courses = must_courses if must_courses is not None else []
        self.recommend_courses = recommend_courses if recommend_courses is not None else []


class LeveledCourse:
    def __init__(self, course: Course, level: int):
        self.course = course
        self.level = level

class TestTopologicalSort(unittest.TestCase):

    def test_empty_list(self):
        """ Test sorting with no courses """
        courses = []
        self.assertEqual(topological_sort(courses), [])

    def test_single_course(self):
        """ Test sorting with one course that has no dependencies """
        courses = [Course("101")]
        sorted_courses = topological_sort(courses)
        self.assertEqual(len(sorted_courses), 1)
        self.assertEqual(sorted_courses[0].course.id, "101")

    def test_basic_dependency(self):
        """ Test sorting where one course directly depends on another """
        courses = [Course("101"), Course("102", ["101"])]
        sorted_courses = topological_sort(courses)
        self.assertEqual([course.course.id for course in sorted_courses], ["101", "102"])

    def test_complex_dependency(self):
        """ Test a complex scenario with multiple dependencies """
        courses = [
            Course("Math"),
            Course("Advanced Math", ["Math"]),
            Course("Physics", ["Math"], ["Advanced Math"]),
            Course("Chemistry")
        ]
        sorted_courses = topological_sort(courses)
        ids = [course.course.id for course in sorted_courses]
        self.assertTrue(ids.index("Math") < ids.index("Advanced Math"))
        self.assertTrue(ids.index("Math") < ids.index("Physics"))

    def test_cycle_detection(self):
        """ Test detection of cycles in course prerequisites """
        courses = [Course("101", ["102"]), Course("102", ["101"])]
        with self.assertRaises(ValueError):
            topological_sort(courses)
if __name__ == '__main__':
    unittest.main()