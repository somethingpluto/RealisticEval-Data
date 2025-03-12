d
e
f
 
i
s
_
b
r
e
a
k
_
t
i
m
e
(
s
t
a
r
t
_
t
i
m
e
:
 
s
t
r
,
 
e
n
d
_
t
i
m
e
:
 
s
t
r
,
 
c
u
r
r
e
n
t
_
t
i
m
e
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
D
e
t
e
r
m
i
n
e
 
w
h
e
t
h
e
r
 
t
h
e
 
c
u
r
r
e
n
t
 
t
i
m
e
 
i
s
 
w
i
t
h
i
n
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
t
i
m
e
 
r
a
n
g
e
 
(
i
.
e
.
,
 
w
h
e
t
h
e
r
 
i
t
 
i
s
 
a
 
b
r
e
a
k
)
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
_
t
i
m
e
 
(
s
t
r
)
:
 
T
h
e
 
s
t
a
r
t
 
t
i
m
e
 
o
f
 
t
h
e
 
b
r
e
a
k
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
e
n
d
_
t
i
m
e
 
(
s
t
r
)
:
 
T
h
e
 
e
n
d
 
t
i
m
e
 
o
f
 
t
h
e
 
b
r
e
a
k
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
t
i
m
e
 
(
s
t
r
)
:
 
T
h
e
 
c
u
r
r
e
n
t
 
t
i
m
e
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
t
i
m
e
 
=
 
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
s
t
a
r
t
_
t
i
m
e
,
 
"
%
H
:
%
M
"
)


 
 
 
 
e
n
d
_
t
i
m
e
 
=
 
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
e
n
d
_
t
i
m
e
,
 
"
%
H
:
%
M
"
)


 
 
 
 
c
u
r
r
e
n
t
_
t
i
m
e
 
=
 
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
c
u
r
r
e
n
t
_
t
i
m
e
,
 
"
%
H
:
%
M
"
)




 
 
 
 
i
f
 
s
t
a
r
t
_
t
i
m
e
 
<
=
 
e
n
d
_
t
i
m
e
:


 
 
 
 
 
 
 
 
i
f
 
s
t
a
r
t
_
t
i
m
e
 
<
=
 
c
u
r
r
e
n
t
_
t
i
m
e
 
<
=
 
e
n
d
_
t
i
m
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
i
f
 
s
t
a
r
t
_
t
i
m
e
 
<
=
 
c
u
r
r
e
n
t
_
t
i
m
e
 
o
r
 
c
u
r
r
e
n
t
_
t
i
m
e
 
<
=
 
e
n
d
_
t
i
m
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
u
e


 
 
 
 
r
e
t
u
r
n
 
F
a
l
s
e






d
e
f
 
g
e
t
_
b
r
e
a
k
_
t
i
m
e
(
s
t
a
r
t
_
t
i
m
e
:
 
s
t
r
,
 
e
n
d
_
t
i
m
e
:
 
s
t
r
,
 
c
u
r
r
e
n
t
_
t
i
m
e
:
 
s
t
r
)
 
-
>
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
 
t
h
e
 
b
r
e
a
k
 
t
i
m
e
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
t
a
r
t
_
t
i
m
e
 
(
s
t
r
)
:
 
T
h
e
 
s
t
a
r
t
 
t
i
m
e
 
o
f
 
t
h
e
 
b
r
e
a
k
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
e
n
d
_
t
i
m
e
 
(
s
t
r
)
:
 
T
h
e
 
e
n
d
 
t
i
m
e
 
o
f
 
t
h
e
 
b
r
e
a
k
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.


 
 
 
 
 
 
 
 
c
u
r
r
e
n
t
_
t
i
m
e
 
(
s
t
r
)
:
 
T
h
e
 
c
u
r
r
e
n
t
 
t
i
m
e
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
s
t
r
:
 
T
h
e
 
b
r
e
a
k
 
t
i
m
e
 
i
n
 
H
H
:
M
M
 
f
o
r
m
a
t
.


 
 
 
 
"
"
"


 
 
 
 
s
t
a
r
t
_
t
i
m
e
 
=
 
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
s
t
a
r
t
_
t
i
m
e
,
 
"
%
H
:
%
M
"
)


 
 
 
 
e
n
d
_
t
i
m
e
 
=
 
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
e
n
d
_
t
i
m
e
,
 
"
%
H
:
%
M
"
)


 
 
 
 
c
u
r
r
e
n
t
_
t
i
m
e
 
=
 
d
a
t
e
t
i
m
e
.
s
t
r
p
t
i
m
e
(
c
u
r
r
e
n
t
_
t
i
m
e
,
 
"
%
H
:
%
M
"
)




 
 
 
 
i
f
 
s
t
a
r
t
_
t
i
m
e
 
<
=
 
e
n
d
_
t
i
m
e
:


 
 
 
 
 
 
 
 
i
f
 
s
t
a
r
t
_
t
i
m
e
 
<
=
 
c
u
r
r
e
n
t
_
t
i
m
e
 
<
=
 
e
n
d
_
t
i
m
e
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
u
r
r
e
n
t
_
t
i
m
e
.
s
t
r
f
t
i
m
e
(
"
%
H
:
%
M
"
)


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
i
f
 
s
t
a
r
t
_
t
i
m
e
 
<
=
 
c
u
r
r
e
n
t
_
t
i
m
e
 
o
r
 
c
u
r
r
e
n
t
_
t
i
m
e
 
<
=
 
e
n
d
_
t
i
m
e
:
import unittest


class TestIsBreakTime(unittest.TestCase):
    def test_current_time_at_start(self):
        self.assertTrue(is_break_time("09:00", "10:00", "09:00"))

    def test_current_time_within_range(self):
        self.assertTrue(is_break_time("09:00", "10:00", "09:30"))

    def test_current_time_exceeds_end_time(self):
        self.assertFalse(is_break_time("09:00", "10:00", "20:00"))

    def test_current_time_before_break_time(self):
        self.assertFalse(is_break_time("09:00", "10:00", "08:59"))

    def test_current_time_after_break_time(self):
        self.assertFalse(is_break_time("09:00", "10:00", "10:01"))

if __name__ == '__main__':
    unittest.main()