d
e
f
 
i
s
_
v
a
l
i
d
_
c
o
o
r
d
i
n
a
t
e
(
c
o
o
r
d
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
c
o
n
f
o
r
m
s
 
t
o
 
t
h
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
 
i
d
e
n
t
i
f
i
c
a
t
i
o
n
 
s
p
e
c
i
f
i
c
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
o
r
d
:
 
T
h
e
 
c
o
o
r
d
i
n
a
t
e
 
s
t
r
i
n
g
 
t
o
 
c
h
e
c
k
 
(
c
a
n
 
b
e
 
l
a
t
i
t
u
d
e
 
o
r
 
l
o
n
g
i
t
u
d
e
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
b
o
o
l
e
a
n
 
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
o
o
r
d
i
n
a
t
e
 
i
s
 
v
a
l
i
d
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
(
r
"
^
[
0
-
9
]
{
1
,
3
}
(
?
:
\
.
[
0
-
9
]
+
)
?
(
?
:
,
|
°
|
\
s
|
$
)
"
,
 
c
o
o
r
d
)
)






d
e
f
 
i
s
_
v
a
l
i
d
_
c
o
o
r
d
i
n
a
t
e
s
(
c
o
o
r
d
i
n
a
t
e
s
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
c
o
n
f
o
r
m
s
 
t
o
 
t
h
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
 
i
d
e
n
t
i
f
i
c
a
t
i
o
n
 
s
p
e
c
i
f
i
c
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
o
r
d
i
n
a
t
e
s
:
 
T
h
e
 
c
o
o
r
d
i
n
a
t
e
s
 
s
t
r
i
n
g
 
t
o
 
c
h
e
c
k
 
(
c
a
n
 
b
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
b
o
o
l
e
a
n
 
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
o
o
r
d
i
n
a
t
e
s
 
a
r
e
 
v
a
l
i
d
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
(
r
"
^
[
0
-
9
]
{
1
,
3
}
(
?
:
\
.
[
0
-
9
]
+
)
?
(
?
:
,
|
°
|
\
s
|
$
)
[
0
-
9
]
{
1
,
3
}
(
?
:
\
.
[
0
-
9
]
+
)
?
(
?
:
,
|
°
|
\
s
|
$
)
"
,
 
c
o
o
r
d
i
n
a
t
e
s
)
)






d
e
f
 
i
s
_
v
a
l
i
d
_
c
o
o
r
d
i
n
a
t
e
_
p
a
i
r
(
c
o
o
r
d
i
n
a
t
e
s
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
c
o
n
f
o
r
m
s
 
t
o
 
t
h
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
 
i
d
e
n
t
i
f
i
c
a
t
i
o
n
 
s
p
e
c
i
f
i
c
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
o
r
d
i
n
a
t
e
s
:
 
T
h
e
 
c
o
o
r
d
i
n
a
t
e
s
 
s
t
r
i
n
g
 
t
o
 
c
h
e
c
k
 
(
c
a
n
 
b
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
b
o
o
l
e
a
n
 
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
o
o
r
d
i
n
a
t
e
s
 
a
r
e
 
v
a
l
i
d
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
(
r
"
^
[
0
-
9
]
{
1
,
3
}
(
?
:
\
.
[
0
-
9
]
+
)
?
(
?
:
,
|
°
|
\
s
|
$
)
[
0
-
9
]
{
1
,
3
}
(
?
:
\
.
[
0
-
9
]
+
)
?
(
?
:
,
|
°
|
\
s
|
$
)
"
,
 
c
o
o
r
d
i
n
a
t
e
s
)
)






d
e
f
 
i
s
_
v
a
l
i
d
_
c
o
o
r
d
i
n
a
t
e
_
p
a
i
r
s
(
c
o
o
r
d
i
n
a
t
e
s
:
 
s
t
r
)
 
-
>
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
t
h
e
 
s
t
r
i
n
g
 
c
o
n
f
o
r
m
s
 
t
o
 
t
h
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
 
i
d
e
n
t
i
f
i
c
a
t
i
o
n
 
s
p
e
c
i
f
i
c
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
o
r
d
i
n
a
t
e
s
:
 
T
h
e
 
c
o
o
r
d
i
n
a
t
e
s
 
s
t
r
i
n
g
 
t
o
 
c
h
e
c
k
 
(
c
a
n
 
b
e
 
l
a
t
i
t
u
d
e
 
a
n
d
 
l
o
n
g
i
t
u
d
e
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
A
 
b
o
o
l
e
a
n
 
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
o
o
r
d
i
n
a
t
e
s
 
a
r
e
 
v
a
l
i
d
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
 
b
o
o
l
(
r
e
.
m
a
t
c
h
import unittest


class TestIsValidCoordinate(unittest.TestCase):

    def test_valid_latitude_with_direction(self):
        coord = "45.123N"
        self.assertTrue(is_valid_coordinate(coord))

    def test_valid_latitude_without_direction(self):
        coord = "90.0"
        self.assertTrue(is_valid_coordinate(coord))

    def test_valid_longitude_with_direction(self):
        coord = "180.0E"
        self.assertTrue(is_valid_coordinate(coord))

    def test_valid_longitude_without_direction(self):
        coord = "-120.456"
        self.assertTrue(is_valid_coordinate(coord))

    def test_invalid_longitude_exceeding_range(self):
        coord = "-200.5"
        self.assertFalse(is_valid_coordinate(coord))
if __name__ == '__main__':
    unittest.main()