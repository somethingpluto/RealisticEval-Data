d
e
f
 
c
o
n
v
e
r
t
_
r
a
n
g
e
_
t
o
_
c
o
l
o
r
_
y
e
l
l
o
w
_
g
r
e
e
n
_
c
h
a
n
g
e
(
v
a
l
u
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
 
t
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
 
a
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r
 
t
h
a
t
 
t
r
a
n
s
i
t
i
o
n
s


 
 
 
 
f
r
o
m
 
r
e
d
 
t
o
 
y
e
l
l
o
w
 
a
n
d
 
t
h
e
n
 
f
r
o
m
 
y
e
l
l
o
w
 
t
o
 
g
r
e
e
n
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
f
l
o
a
t
)
:
 
A
 
f
l
o
a
t
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
t
e
r
p
o
l
a
t
i
o
n
 
p
o
s
i
t
i
o
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
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
 
R
G
B
 
c
o
l
o
r
 
v
a
l
u
e
s
 
(
r
e
d
,
 
g
r
e
e
n
,
 
b
l
u
e
)
.


 
 
 
 
"
"
"




 
 
 
 
#
 
S
c
a
l
e
 
t
h
e
 
i
n
p
u
t
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
t
o
 
[
0
,
 
2
5
5
]


 
 
 
 
v
a
l
u
e
 
=
 
v
a
l
u
e
 
*
 
2
5
5




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
i
n
p
u
t
 
v
a
l
u
e
 
t
o
 
a
 
h
u
e
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]


 
 
 
 
h
u
e
 
=
 
v
a
l
u
e
 
/
 
2
5
5




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
h
u
e
 
v
a
l
u
e
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r


 
 
 
 
r
e
d
,
 
g
r
e
e
n
,
 
b
l
u
e
 
=
 
h
s
v
_
t
o
_
r
g
b
(
h
u
e
,
 
1
,
 
1
)




 
 
 
 
r
e
t
u
r
n
 
r
e
d
,
 
g
r
e
e
n
,
 
b
l
u
e






d
e
f
 
c
o
n
v
e
r
t
_
r
a
n
g
e
_
t
o
_
c
o
l
o
r
_
y
e
l
l
o
w
_
g
r
e
e
n
_
c
h
a
n
g
e
_
i
n
v
e
r
t
e
d
(
v
a
l
u
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
 
t
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
 
a
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r
 
t
h
a
t
 
t
r
a
n
s
i
t
i
o
n
s


 
 
 
 
f
r
o
m
 
r
e
d
 
t
o
 
y
e
l
l
o
w
 
a
n
d
 
t
h
e
n
 
f
r
o
m
 
y
e
l
l
o
w
 
t
o
 
g
r
e
e
n
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
f
l
o
a
t
)
:
 
A
 
f
l
o
a
t
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
n
t
e
r
p
o
l
a
t
i
o
n
 
p
o
s
i
t
i
o
n
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
t
u
p
l
e
:
 
A
 
t
u
p
l
e
 
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
 
R
G
B
 
c
o
l
o
r
 
v
a
l
u
e
s
 
(
r
e
d
,
 
g
r
e
e
n
,
 
b
l
u
e
)
.


 
 
 
 
"
"
"




 
 
 
 
#
 
S
c
a
l
e
 
t
h
e
 
i
n
p
u
t
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
t
o
 
[
0
,
 
2
5
5
]


 
 
 
 
v
a
l
u
e
 
=
 
v
a
l
u
e
 
*
 
2
5
5




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
i
n
p
u
t
 
v
a
l
u
e
 
t
o
 
a
 
h
u
e
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]


 
 
 
 
h
u
e
 
=
 
1
 
-
 
(
v
a
l
u
e
 
/
 
2
5
5
)




 
 
 
 
#
 
C
o
n
v
e
r
t
 
t
h
e
 
h
u
e
 
v
a
l
u
e
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r


 
 
 
 
r
e
d
,
 
g
r
e
e
n
,
 
b
l
u
e
 
=
 
h
s
v
_
t
o
_
r
g
b
(
h
u
e
,
 
1
,
 
1
)




 
 
 
 
r
e
t
u
r
n
 
r
e
d
,
 
g
r
e
e
n
,
 
b
l
u
e






d
e
f
 
c
o
n
v
e
r
t
_
r
a
n
g
e
_
t
o
_
c
o
l
o
r
_
y
e
l
l
o
w
_
g
r
e
e
n
_
c
h
a
n
g
e
_
i
n
v
e
r
t
e
d
_
w
i
t
h
_
o
f
f
s
e
t
(
v
a
l
u
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
 
t
u
p
l
e
:


 
 
 
 
"
"
"


 
 
 
 
C
o
n
v
e
r
t
 
a
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
t
o
 
a
n
 
R
G
B
 
c
o
l
o
r
 
t
h
a
t
 
t
r
a
n
s
i
t
i
o
n
s


 
 
 
 
f
r
o
m
 
r
e
d
 
t
o
 
y
e
l
l
o
w
 
a
n
d
 
t
h
e
n
 
f
r
o
m
 
y
e
l
l
o
w
 
t
o
 
g
r
e
e
n
.




 
 
 
 
P
a
r
a
m
e
t
e
r
s
:


 
 
 
 
 
 
 
 
v
a
l
u
e
 
(
f
l
o
a
t
)
:
 
A
 
f
l
o
a
t
 
v
a
l
u
e
 
i
n
 
t
h
e
 
r
a
n
g
e
 
[
0
,
 
1
]
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
import unittest
class TestConvertToColorThroughYellow(unittest.TestCase):
    
    def test_red(self):
        """Test the output for value 0.0 (should be red)"""
        self.assertEqual(convert_to_color_through_yellow(0.0), (255, 127.5, 127.5))

    def test_yellow(self):
        """Test the output for value 0.5 (should be yellow)"""
        self.assertEqual(convert_to_color_through_yellow(0.5), (255, 255, 127.5))

    def test_green(self):
        """Test the output for value 1.0 (should be green)"""
        self.assertEqual(convert_to_color_through_yellow(1.0), (0, 255, 127.5))

    def test_mid_transition(self):
        """Test the output for value 0.25 (between red and yellow)"""
        self.assertEqual(convert_to_color_through_yellow(0.25), (255, 191, 127.5))

    def test_yellow_transition(self):
        """Test the output for value 0.75 (between yellow and green)"""
        self.assertEqual(convert_to_color_through_yellow(0.75), (127, 255, 127.5))
if __name__ == '__main__':
    unittest.main()