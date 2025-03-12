d
e
f
 
c
o
u
n
t
_
u
n
i
q
u
e
_
c
o
l
o
r
s
(
i
m
a
g
e
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
a
n
 
i
m
a
g
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
m
a
g
e
_
p
a
t
h
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
i
m
a
g
e
 
f
i
l
e
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
t
h
e
 
i
m
a
g
e
.


 
 
 
 
"
"
"


 
 
 
 
i
m
a
g
e
 
=
 
I
m
a
g
e
.
o
p
e
n
(
i
m
a
g
e
_
p
a
t
h
)


 
 
 
 
i
m
a
g
e
 
=
 
i
m
a
g
e
.
c
o
n
v
e
r
t
(
"
R
G
B
"
)


 
 
 
 
u
n
i
q
u
e
_
c
o
l
o
r
s
 
=
 
s
e
t
(
i
m
a
g
e
.
g
e
t
d
a
t
a
(
)
)


 
 
 
 
r
e
t
u
r
n
 
l
e
n
(
u
n
i
q
u
e
_
c
o
l
o
r
s
)






d
e
f
 
c
o
u
n
t
_
u
n
i
q
u
e
_
c
o
l
o
r
s
_
i
n
_
f
o
l
d
e
r
(
f
o
l
d
e
r
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
a
l
l
 
i
m
a
g
e
s
 
i
n
 
a
 
f
o
l
d
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
o
l
d
e
r
_
p
a
t
h
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
f
o
l
d
e
r
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
i
m
a
g
e
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
a
l
l
 
i
m
a
g
e
s
 
i
n
 
t
h
e
 
f
o
l
d
e
r
.


 
 
 
 
"
"
"


 
 
 
 
i
m
a
g
e
_
p
a
t
h
s
 
=
 
g
e
t
_
i
m
a
g
e
_
p
a
t
h
s
_
i
n
_
f
o
l
d
e
r
(
f
o
l
d
e
r
_
p
a
t
h
)


 
 
 
 
u
n
i
q
u
e
_
c
o
l
o
r
s
 
=
 
s
e
t
(
)


 
 
 
 
f
o
r
 
i
m
a
g
e
_
p
a
t
h
 
i
n
 
i
m
a
g
e
_
p
a
t
h
s
:


 
 
 
 
 
 
 
 
u
n
i
q
u
e
_
c
o
l
o
r
s
.
u
p
d
a
t
e
(
c
o
u
n
t
_
u
n
i
q
u
e
_
c
o
l
o
r
s
(
i
m
a
g
e
_
p
a
t
h
)
)


 
 
 
 
r
e
t
u
r
n
 
l
e
n
(
u
n
i
q
u
e
_
c
o
l
o
r
s
)






d
e
f
 
c
o
u
n
t
_
u
n
i
q
u
e
_
c
o
l
o
r
s
_
i
n
_
s
u
b
f
o
l
d
e
r
s
(
f
o
l
d
e
r
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
a
l
l
 
i
m
a
g
e
s
 
i
n
 
a
l
l
 
s
u
b
f
o
l
d
e
r
s
 
o
f
 
a
 
f
o
l
d
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
o
l
d
e
r
_
p
a
t
h
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
f
o
l
d
e
r
 
c
o
n
t
a
i
n
i
n
g
 
t
h
e
 
s
u
b
f
o
l
d
e
r
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


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
a
l
l
 
i
m
a
g
e
s
 
i
n
 
a
l
l
 
s
u
b
f
o
l
d
e
r
s
 
o
f
 
t
h
e
 
f
o
l
d
e
r
.


 
 
 
 
"
"
"


 
 
 
 
s
u
b
f
o
l
d
e
r
_
p
a
t
h
s
 
=
 
g
e
t
_
s
u
b
f
o
l
d
e
r
_
p
a
t
h
s
_
i
n
_
f
o
l
d
e
r
(
f
o
l
d
e
r
_
p
a
t
h
)


 
 
 
 
u
n
i
q
u
e
_
c
o
l
o
r
s
 
=
 
s
e
t
(
)


 
 
 
 
f
o
r
 
s
u
b
f
o
l
d
e
r
_
p
a
t
h
 
i
n
 
s
u
b
f
o
l
d
e
r
_
p
a
t
h
s
:


 
 
 
 
 
 
 
 
u
n
i
q
u
e
_
c
o
l
o
r
s
.
u
p
d
a
t
e
(
c
o
u
n
t
_
u
n
i
q
u
e
_
c
o
l
o
r
s
_
i
n
_
f
o
l
d
e
r
(
s
u
b
f
o
l
d
e
r
_
p
a
t
h
)
)


 
 
 
 
r
e
t
u
r
n
 
l
e
n
(
u
n
i
q
u
e
_
c
o
l
o
r
s
)






d
e
f
 
c
o
u
n
t
_
u
n
i
q
u
e
_
c
o
l
o
r
s
_
i
n
_
s
u
b
f
o
l
d
e
r
s
_
o
f
_
s
u
b
f
o
l
d
e
r
s
(
f
o
l
d
e
r
_
p
a
t
h
:
 
s
t
r
)
 
-
>
 
i
n
t
:


 
 
 
 
"
"
"


 
 
 
 
C
o
u
n
t
 
t
h
e
 
n
u
m
b
e
r
 
o
f
 
u
n
i
q
u
e
 
c
o
l
o
r
s
 
i
n
 
a
l
l
 
i
m
a
g
e
s
 
i
n
 
a
l
l
 
s
u
b
f
o
l
d
e
r
s
 
o
f
 
a
l
l
 
s
u
b
f
o
l
d
e
r
s
import unittest


class TestCountUniqueColor(unittest.TestCase):

    def test_case1(self):
        picture_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase01.png"
        expected_color_num = 1
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case2(self):
        picture_path = r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase02.png"
        expected_color_num = 2
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)

    def test_case3(self):
        picture_path =r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase03.png"
        expected_color_num = 3
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)
    def test_case4(self):
        picture_path =r"E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase04.png"
        expected_color_num = 466
        output = count_unique_colors(picture_path)
        self.assertEqual(output, expected_color_num)
if __name__ == '__main__':
    unittest.main()