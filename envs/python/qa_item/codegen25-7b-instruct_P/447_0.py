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
 
U
n
i
o
n






d
e
f
 
c
a
l
c
u
l
a
t
e
_
a
g
e
(
b
i
r
t
h
_
d
a
t
e
_
s
t
r
i
n
g
:
 
s
t
r
)
 
-
>
 
U
n
i
o
n
[
s
t
r
,
i
n
t
]
:


 
 
 
 
"
"
"


 
 
 
 
C
a
l
c
u
l
a
t
e
 
a
g
e
 
b
a
s
e
d
 
o
n
 
t
h
e
 
b
i
r
t
h
 
d
a
t
e
 
s
t
r
i
n
g
 
e
n
t
e
r
e
d
 
b
y
 
t
h
e
 
u
s
e
r
.




 
 
 
 
I
n
p
u
t
 
b
i
r
t
h
_
d
a
t
e
_
s
t
r
i
n
g
 
f
o
r
m
a
t
 
s
u
c
h
 
a
s
 
"
2
0
0
0
-
0
1
-
0
1
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
b
i
r
t
h
_
d
a
t
e
_
s
t
r
i
n
g
 
(
s
t
r
)
:
 
T
h
e
 
b
i
r
t
h
 
d
a
t
e
 
i
n
 
s
t
r
i
n
g
 
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
 
|
 
i
n
t
:
 
T
h
e
 
a
g
e
 
a
s
 
a
n
 
i
n
t
e
g
e
r
 
o
r
 
a
n
 
e
r
r
o
r
 
m
e
s
s
a
g
e
 
a
s
 
a
 
s
t
r
i
n
g


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
t
h
e
 
d
a
t
e
 
f
o
r
m
a
t
 
i
s
 
i
n
v
a
l
i
d
.


 
 
 
 
"
"
"


 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
b
i
r
t
h
_
d
a
t
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
b
i
r
t
h
_
d
a
t
e
_
s
t
r
i
n
g
,
 
"
%
Y
-
%
m
-
%
d
"
)


 
 
 
 
 
 
 
 
t
o
d
a
y
 
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
n
o
w
(
)


 
 
 
 
 
 
 
 
a
g
e
 
=
 
t
o
d
a
y
.
y
e
a
r
 
-
 
b
i
r
t
h
_
d
a
t
e
.
y
e
a
r
 
-
 
(
(
t
o
d
a
y
.
m
o
n
t
h
,
 
t
o
d
a
y
.
d
a
y
)
 
<
 
(
b
i
r
t
h
_
d
a
t
e
.
m
o
n
t
h
,
 
b
i
r
t
h
_
d
a
t
e
.
d
a
y
)
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
a
g
e


 
 
 
 
e
x
c
e
p
t
 
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


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
I
n
v
a
l
i
d
 
d
a
t
e
 
f
o
r
m
a
t
.
 
P
l
e
a
s
e
 
e
n
t
e
r
 
d
a
t
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
o
f
 
Y
Y
Y
Y
-
M
M
-
D
D
.
"




#
 
T
e
s
t
 
c
a
s
e
s


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
0
0
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
1


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
1
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
0


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
2
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
1


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
3
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
2


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
4
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
3


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
5
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
4


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
6
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
5


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
7
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
6


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
8
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
7


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
2
9
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
8


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
3
0
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
9


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
3
1
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
1
0


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
3
2
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
:
 
1
1


p
r
i
n
t
(
c
a
l
c
u
l
a
t
e
_
a
g
e
(
"
2
0
3
3
-
0
1
-
0
1
"
)
)
 
#
 
O
u
t
p
u
t
from datetime import datetime, timedelta
import unittest


class TestCalculateAge(unittest.TestCase):

    def test_calculates_age_correctly_for_a_birth_date_in_the_past(self):
        self.assertEqual(calculate_age('2000-01-01'), datetime.now().year - 2000)

    def test_calculates_age_correctly_for_a_birth_date_in_the_long_past(self):
        self.assertEqual(calculate_age('1000-01-01'), datetime.now().year - 1000)

    def test_calculates_age_correctly_for_a_birth_date_today(self):
        today = datetime.now().strftime('%Y-%m-%d')  # Get today's date in YYYY-MM-DD format
        self.assertEqual(calculate_age(today), 0)

    def test_calculates_age_correctly_for_a_person_born_yesterday(self):
        yesterday = datetime.now() - timedelta(days=1)  # Set to yesterday
        birth_date_string = yesterday.strftime('%Y-%m-%d')  # Format as YYYY-MM-DD
        self.assertEqual(calculate_age(birth_date_string), 0)

if __name__ == '__main__':
    unittest.main()