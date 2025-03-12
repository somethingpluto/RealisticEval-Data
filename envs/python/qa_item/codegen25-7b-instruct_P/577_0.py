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
p
o
s
t
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
 
p
o
s
t
 
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
 
p
o
s
t
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
P
o
s
t
"
 
o
r
 
"
P
o
s
t
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
2
 
P
o
s
t
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
 
P
o
s
t
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
 
p
o
s
t
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
 
p
o
s
t
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
 
P
o
s
t
"
 
o
r
 
"
X
X
 
P
o
s
t
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
 
{
'
P
o
s
t
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
P
o
s
t
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
p
o
s
t
_
c
o
u
n
t
_
w
i
t
h
_
c
o
m
m
a
s
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
 
p
o
s
t
 
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
 
p
o
s
t
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
P
o
s
t
"
 
o
r
 
"
P
o
s
t
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
,
0
0
0
 
P
o
s
t
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
,
0
0
0
 
P
o
s
t
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
 
p
o
s
t
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
 
p
o
s
t
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
,
0
0
0
 
P
o
s
t
"
 
o
r
 
"
X
X
,
0
0
0
 
P
o
s
t
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
h
r
e
e
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
,
d
}
 
{
'
P
o
s
t
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
P
o
s
t
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
p
o
s
t
_
c
o
u
n
t
_
w
i
t
h
_
c
o
m
m
a
s
_
a
n
d
_
s
u
f
f
i
x
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
,
 
s
u
f
f
i
x
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
 
p
o
s
t
 
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
 
p
o
s
t
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
P
o
s
t
"
 
o
r
 
"
P
o
s
t
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
,
0
0
0
 
P
o
s
t
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
,
0
0
0
 
P
o
s
t
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
import unittest


class TestFormatPostCount(unittest.TestCase):

    def test_return_one_post(self):
        """Should return "01 Post" for count of 1."""
        self.assertEqual(format_post_count(1), "01 Post")

    def test_return_two_posts(self):
        """Should return "02 Posts" for count of 2."""
        self.assertEqual(format_post_count(2), "02 Posts")

    def test_return_ten_posts(self):
        """Should return "10 Posts" for count of 10."""
        self.assertEqual(format_post_count(10), "10 Posts")

    def test_return_ninety_nine_posts(self):
        """Should return "99 Posts" for count of 99."""
        self.assertEqual(format_post_count(99), "99 Posts")

    def test_return_five_posts(self):
        """Should return "05 Posts" for count of 5."""
        self.assertEqual(format_post_count(5), "05 Posts")

if __name__ == '__main__':
    unittest.main()