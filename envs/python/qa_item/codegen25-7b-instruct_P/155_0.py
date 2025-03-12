f
r
o
m
 
d
a
t
e
t
i
m
e
 
i
m
p
o
r
t
 
d
a
t
e
t
i
m
e






d
e
f
 
g
e
t
_
t
i
m
e
s
t
a
m
p
(
c
r
e
a
t
e
d
_
a
t
:
 
d
a
t
e
t
i
m
e
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
C
o
m
p
u
t
e
s
 
t
h
e
 
d
i
f
f
e
r
e
n
c
e
 
b
e
t
w
e
e
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
 
d
a
t
e
 
a
n
d
 
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
,
 
r
e
t
u
r
n
i
n
g
 
i
t
 
i
n
 
a
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
w
a
y
.


 
 
 
 


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
r
e
a
t
e
d
_
a
t
 
(
d
a
t
e
t
i
m
e
)
:
 
T
h
e
 
d
a
t
e
 
t
o
 
c
a
l
c
u
l
a
t
e
 
t
h
e
 
t
i
m
e
 
d
i
f
f
e
r
e
n
c
e
 
f
r
o
m
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
 
A
 
s
t
r
i
n
g
 
i
n
d
i
c
a
t
i
n
g
 
t
h
e
 
t
i
m
e
 
e
l
a
p
s
e
d
,
 
e
.
g
.
,
 
"
3
 
d
a
y
s
 
a
g
o
"
,
 
"
5
 
h
o
u
r
s
 
a
g
o
"
.


 
 
 
 
"
"
"


 
 
 
 
n
o
w
 
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
u
t
c
n
o
w
(
)


 
 
 
 
d
i
f
f
 
=
 
n
o
w
 
-
 
c
r
e
a
t
e
d
_
a
t


 
 
 
 
s
e
c
o
n
d
_
d
i
f
f
 
=
 
d
i
f
f
.
s
e
c
o
n
d
s


 
 
 
 
d
a
y
_
d
i
f
f
 
=
 
d
i
f
f
.
d
a
y
s




 
 
 
 
i
f
 
d
a
y
_
d
i
f
f
 
<
 
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
'




 
 
 
 
i
f
 
d
a
y
_
d
i
f
f
 
=
=
 
0
:


 
 
 
 
 
 
 
 
i
f
 
s
e
c
o
n
d
_
d
i
f
f
 
<
 
1
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
j
u
s
t
 
n
o
w
"


 
 
 
 
 
 
 
 
i
f
 
s
e
c
o
n
d
_
d
i
f
f
 
<
 
6
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
s
e
c
o
n
d
_
d
i
f
f
)
 
+
 
"
 
s
e
c
o
n
d
s
 
a
g
o
"


 
 
 
 
 
 
 
 
i
f
 
s
e
c
o
n
d
_
d
i
f
f
 
<
 
1
2
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
a
 
m
i
n
u
t
e
 
a
g
o
"


 
 
 
 
 
 
 
 
i
f
 
s
e
c
o
n
d
_
d
i
f
f
 
<
 
3
6
0
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
s
e
c
o
n
d
_
d
i
f
f
 
/
/
 
6
0
)
 
+
 
"
 
m
i
n
u
t
e
s
 
a
g
o
"


 
 
 
 
 
 
 
 
i
f
 
s
e
c
o
n
d
_
d
i
f
f
 
<
 
7
2
0
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
a
n
 
h
o
u
r
 
a
g
o
"


 
 
 
 
 
 
 
 
i
f
 
s
e
c
o
n
d
_
d
i
f
f
 
<
 
8
6
4
0
0
:


 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
s
e
c
o
n
d
_
d
i
f
f
 
/
/
 
3
6
0
0
)
 
+
 
"
 
h
o
u
r
s
 
a
g
o
"


 
 
 
 
i
f
 
d
a
y
_
d
i
f
f
 
=
=
 
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
y
e
s
t
e
r
d
a
y
"


 
 
 
 
i
f
 
d
a
y
_
d
i
f
f
 
<
 
7
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
d
a
y
_
d
i
f
f
)
 
+
 
"
 
d
a
y
s
 
a
g
o
"


 
 
 
 
i
f
 
d
a
y
_
d
i
f
f
 
<
 
3
1
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
d
a
y
_
d
i
f
f
 
/
/
 
7
)
 
+
 
"
 
w
e
e
k
s
 
a
g
o
"


 
 
 
 
i
f
 
d
a
y
_
d
i
f
f
 
<
 
3
6
5
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
d
a
y
_
d
i
f
f
 
/
/
 
3
0
)
 
+
 
"
 
m
o
n
t
h
s
 
a
g
o
"


 
 
 
 
r
e
t
u
r
n
 
s
t
r
(
d
a
y
_
d
i
f
f
 
/
/
 
3
6
5
)
 
+
 
"
 
y
e
a
r
s
 
a
g
o
"


import unittest
from datetime import datetime, timedelta

class TestGetTimestamp(unittest.TestCase):

    def test_one_second_ago(self):
        one_second_ago = datetime.now() - timedelta(seconds=1)  # 1 second ago
        self.assertEqual(get_timestamp(one_second_ago), '1 second ago')

    def test_five_minutes_ago(self):
        five_minutes_ago = datetime.now() - timedelta(minutes=5)  # 5 minutes ago
        self.assertEqual(get_timestamp(five_minutes_ago), '5 minutes ago')

    def test_two_hours_ago(self):
        two_hours_ago = datetime.now() - timedelta(hours=2)  # 2 hours ago
        self.assertEqual(get_timestamp(two_hours_ago), '2 hours ago')

    def test_three_days_ago(self):
        three_days_ago = datetime.now() - timedelta(days=3)  # 3 days ago
        self.assertEqual(get_timestamp(three_days_ago), '3 days ago')
if __name__ == '__main__':
    unittest.main()