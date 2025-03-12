d
e
f
 
f
o
r
m
a
t
_
t
h
r
e
a
d
_
c
o
u
n
t
(
c
o
u
n
t
:
 
i
n
t
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


 
 
 
 
F
o
r
m
a
t
s
 
t
h
e
 
t
h
r
e
a
d
 
c
o
u
n
t
 
i
n
t
o
 
a
 
u
s
e
r
-
f
r
i
e
n
d
l
y
 
s
t
r
i
n
g
.




 
 
 
 
T
h
e
 
f
u
n
c
t
i
o
n
 
f
o
r
m
a
t
s
 
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
 
t
h
r
e
a
d
s
 
i
n
t
o
 
a
 
t
w
o
-
d
i
g
i
t
 
s
t
r
i
n
g


 
 
 
 
f
o
l
l
o
w
e
d
 
b
y
 
"
T
h
r
e
a
d
"
 
o
r
 
"
T
h
r
e
a
d
s
"
 
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
 
c
o
u
n
t
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
3
 
 
O
u
t
p
u
t
:
 
"
0
3
 
T
h
r
e
a
d
s
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
 
 
O
u
t
p
u
t
:
 
"
0
1
 
T
h
r
e
a
d
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
u
n
t
 
(
i
n
t
)
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
 
t
h
r
e
a
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
f
o
r
m
a
t
t
e
d
 
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
 
n
u
m
b
e
r
 
o
f
 
t
h
r
e
a
d
s
.


 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
r
i
n
g
 
w
i
l
l
 
b
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
 
"
X
X
 
T
h
r
e
a
d
"
 
o
r
 
"
X
X
 
T
h
r
e
a
d
s
"
,


 
 
 
 
 
 
 
 
 
 
 
 
 
w
h
e
r
e
 
X
X
 
i
s
 
t
h
e
 
c
o
u
n
t
 
f
o
r
m
a
t
t
e
d
 
a
s
 
a
 
t
w
o
-
d
i
g
i
t
 
n
u
m
b
e
r
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
f
"
{
c
o
u
n
t
:
0
2
d
}
 
T
h
r
e
a
d
{
'
s
'
 
i
f
 
c
o
u
n
t
 
!
=
 
1
 
e
l
s
e
 
'
'
}
"






d
e
f
 
f
o
r
m
a
t
_
t
i
m
e
(
t
i
m
e
:
 
f
l
o
a
t
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


 
 
 
 
F
o
r
m
a
t
s
 
t
h
e
 
t
i
m
e
 
i
n
t
o
 
a
 
u
s
e
r
-
f
r
i
e
n
d
l
y
 
s
t
r
i
n
g
.




 
 
 
 
T
h
e
 
f
u
n
c
t
i
o
n
 
f
o
r
m
a
t
s
 
t
h
e
 
t
i
m
e
 
i
n
t
o
 
a
 
t
w
o
-
d
i
g
i
t
 
s
t
r
i
n
g
 
f
o
l
l
o
w
e
d
 
b
y


 
 
 
 
"
S
e
c
o
n
d
"
 
o
r
 
"
S
e
c
o
n
d
s
"
 
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
 
c
o
u
n
t
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
3
.
5
 
 
O
u
t
p
u
t
:
 
"
0
3
.
5
0
 
S
e
c
o
n
d
s
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
.
0
 
 
O
u
t
p
u
t
:
 
"
0
1
.
0
0
 
S
e
c
o
n
d
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
i
m
e
 
(
f
l
o
a
t
)
:
 
T
h
e
 
t
i
m
e
 
i
n
 
s
e
c
o
n
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
f
o
r
m
a
t
t
e
d
 
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
.


 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
s
t
r
i
n
g
 
w
i
l
l
 
b
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
 
"
X
X
.
X
X
 
S
e
c
o
n
d
s
"
 
o
r


 
 
 
 
 
 
 
 
 
 
 
 
 
"
X
X
.
X
X
 
S
e
c
o
n
d
"
,
 
w
h
e
r
e
 
X
X
.
X
X
 
i
s
 
t
h
e
 
t
i
m
e
 
f
o
r
m
a
t
t
e
d
 
a
s
 
a


 
 
 
 
 
 
 
 
 
 
 
 
 
t
w
o
-
d
i
g
i
t
 
n
u
m
b
e
r
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
f
"
{
t
i
m
e
:
.
2
f
}
 
{
'
S
e
c
o
n
d
'
 
i
f
 
t
i
m
e
 
=
=
 
1
 
e
l
s
e
 
'
S
e
c
o
n
d
s
'
}
"






d
e
f
 
f
o
r
m
a
t
_
s
i
z
e
(
s
i
z
e
:
 
i
n
t
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


 
 
 
 
F
o
r
m
a
t
s
 
t
h
e
 
s
i
z
e
 
i
n
t
o
 
a
 
u
s
e
r
-
f
r
i
e
n
d
l
y
 
s
t
r
i
n
g
.




 
 
 
 
T
h
e
 
f
u
n
c
t
i
o
n
 
f
o
r
m
a
t
s
 
t
h
e
 
s
i
z
e
 
i
n
t
o
 
a
 
t
w
o
-
d
i
g
i
t
 
s
t
r
i
n
g
 
f
o
l
l
o
w
e
d
 
b
y


 
 
 
 
"
B
y
t
e
"
 
o
r
 
"
B
y
t
e
s
"
 
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
 
c
o
u
n
t
.




 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
3
 
 
O
u
t
p
u
t
:
 
"
0
3
 
B
y
t
e
s
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
 
 
O
u
t
p
u
t
:
 
"
0
1
 
B
y
t
e
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
i
z
e
 
(
i
n
t
)
:
 
T
h
e
 
s
i
z
e
 
i
n
 
b
y
t
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


 
 
 
 
 
 
 
 
s
t
r
:
 
A
 
f
o
r
m
a
t
t
e
d
 
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
 
s
i
z
e
.


 
 
 
 
 
 
 
 
 
 
 
 
import unittest


class TestFormatThreadCount(unittest.TestCase):

    def test_count_of_one(self):
        """should return '01 Thread' for a count of 1"""
        self.assertEqual(format_thread_count(1), "01 Thread")

    def test_count_of_five(self):
        """should return '05 Threads' for a count of 5"""
        self.assertEqual(format_thread_count(5), "05 Threads")

    def test_count_of_ten(self):
        """should return '10 Threads' for a count of 10"""
        self.assertEqual(format_thread_count(10), "10 Threads")

    def test_count_of_ninety_nine(self):
        """should return '99 Threads' for a count of 99"""
        self.assertEqual(format_thread_count(99), "99 Threads")
if __name__ == '__main__':
    unittest.main()