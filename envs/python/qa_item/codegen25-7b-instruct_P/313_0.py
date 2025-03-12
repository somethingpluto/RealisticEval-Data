d
e
f
 
i
s
_
b
a
c
k
g
r
o
u
n
d
_
t
o
o
_
d
a
r
k
_
o
r
_
b
r
i
g
h
t
(
c
o
m
p
u
t
e
d
_
s
t
y
l
e
)
:


 
 
 
 
"
"
"
D
e
t
e
c
t
i
n
g
 
t
h
e
 
l
i
g
h
t
 
o
r
 
d
a
r
k
 
s
t
a
t
e
 
o
f
 
t
h
e
 
b
a
c
k
g
r
o
u
n
d
 
e
l
e
m
e
n
t
 
a
n
d
 
r
e
t
u
r
n
i
n
g
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
d
e
s
c
r
i
p
t
i
o
n
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
m
p
u
t
e
d
_
s
t
y
l
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
o
m
p
u
t
e
d
 
b
a
c
k
g
r
o
u
n
d
 
c
o
l
o
r
 
i
n
 
'
r
g
b
(
r
,
 
g
,
 
b
)
'
 
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
 
"
d
a
r
k
"
 
i
f
 
t
h
e
 
b
a
c
k
g
r
o
u
n
d
 
i
s
 
t
o
o
 
d
a
r
k
,
 
"
b
r
i
g
h
t
"
 
i
f
 
i
t
 
i
s
 
t
o
o
 
b
r
i
g
h
t
,
 
o
r
 
"
n
o
r
m
a
l
"
 
i
f
 
i
t
 
i
s
 
n
e
i
t
h
e
r
.


 
 
 
 
"
"
"


 
 
 
 
r
,
 
g
,
 
b
 
=
 
[
i
n
t
(
x
)
 
f
o
r
 
x
 
i
n
 
c
o
m
p
u
t
e
d
_
s
t
y
l
e
[
4
:
-
1
]
.
s
p
l
i
t
(
'
,
'
)
]


 
 
 
 
i
f
 
r
 
>
 
2
0
0
 
a
n
d
 
g
 
>
 
2
0
0
 
a
n
d
 
b
 
>
 
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
 
'
b
r
i
g
h
t
'


 
 
 
 
e
l
i
f
 
r
 
<
 
5
0
 
a
n
d
 
g
 
<
 
5
0
 
a
n
d
 
b
 
<
 
5
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
d
a
r
k
'


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
n
o
r
m
a
l
'






d
e
f
 
i
s
_
t
e
x
t
_
t
o
o
_
d
a
r
k
_
o
r
_
b
r
i
g
h
t
(
c
o
m
p
u
t
e
d
_
s
t
y
l
e
)
:


 
 
 
 
"
"
"
D
e
t
e
c
t
i
n
g
 
t
h
e
 
l
i
g
h
t
 
o
r
 
d
a
r
k
 
s
t
a
t
e
 
o
f
 
t
h
e
 
t
e
x
t
 
e
l
e
m
e
n
t
 
a
n
d
 
r
e
t
u
r
n
i
n
g
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
d
e
s
c
r
i
p
t
i
o
n
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
m
p
u
t
e
d
_
s
t
y
l
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
o
m
p
u
t
e
d
 
t
e
x
t
 
c
o
l
o
r
 
i
n
 
'
r
g
b
(
r
,
 
g
,
 
b
)
'
 
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
 
"
d
a
r
k
"
 
i
f
 
t
h
e
 
t
e
x
t
 
i
s
 
t
o
o
 
d
a
r
k
,
 
"
b
r
i
g
h
t
"
 
i
f
 
i
t
 
i
s
 
t
o
o
 
b
r
i
g
h
t
,
 
o
r
 
"
n
o
r
m
a
l
"
 
i
f
 
i
t
 
i
s
 
n
e
i
t
h
e
r
.


 
 
 
 
"
"
"


 
 
 
 
r
,
 
g
,
 
b
 
=
 
[
i
n
t
(
x
)
 
f
o
r
 
x
 
i
n
 
c
o
m
p
u
t
e
d
_
s
t
y
l
e
[
4
:
-
1
]
.
s
p
l
i
t
(
'
,
'
)
]


 
 
 
 
i
f
 
r
 
>
 
2
0
0
 
a
n
d
 
g
 
>
 
2
0
0
 
a
n
d
 
b
 
>
 
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
 
'
b
r
i
g
h
t
'


 
 
 
 
e
l
i
f
 
r
 
<
 
5
0
 
a
n
d
 
g
 
<
 
5
0
 
a
n
d
 
b
 
<
 
5
0
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
d
a
r
k
'


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
n
o
r
m
a
l
'






d
e
f
 
i
s
_
e
l
e
m
e
n
t
_
v
i
s
i
b
l
e
(
c
o
m
p
u
t
e
d
_
s
t
y
l
e
)
:


 
 
 
 
"
"
"
D
e
t
e
c
t
i
n
g
 
t
h
e
 
v
i
s
i
b
i
l
i
t
y
 
o
f
 
t
h
e
 
e
l
e
m
e
n
t
 
a
n
d
 
r
e
t
u
r
n
i
n
g
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
d
e
s
c
r
i
p
t
i
o
n
 
s
t
r
i
n
g
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
c
o
m
p
u
t
e
d
_
s
t
y
l
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
o
m
p
u
t
e
d
 
s
t
y
l
e
 
o
f
 
t
h
e
 
e
l
e
m
e
n
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
 
"
v
i
s
i
b
l
e
"
 
i
f
 
t
h
e
 
e
l
e
m
e
n
t
 
i
s
 
v
i
s
i
b
l
e
,
 
"
h
i
d
d
e
n
"
 
i
f
 
i
t
 
i
s
 
h
i
d
d
e
n
,
 
o
r
 
"
c
o
l
l
a
p
s
e
d
"
 
i
f
 
i
t
 
i
s
 
c
o
l
l
a
p
s
e
d
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
c
o
m
p
u
t
e
d
_
s
t
y
l
e
 
=
=
 
'
n
o
n
e
'
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
h
i
d
d
e
n
'


 
 
 
 
e
l
i
f
 
c
o
m
p
u
t
e
d
_
s
t
y
l
e
 
=
=
 
'
h
i
d
d
e
n
'
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
h
i
d
d
e
n
'


 
 
 
 
e
l
i
f
 
c
o
m
p
u
t
e
d
_
s
t
y
l
e
 
=
=
class TestBackgroundBrightness(unittest.TestCase):
    def test_dark_background(self):
        """Test for a dark background color."""
        background_color = 'rgb(30, 30, 30)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'dark')

    def test_bright_background(self):
        """Test for a bright background color."""
        background_color = 'rgb(250, 250, 250)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'bright')

    def test_normal_background(self):
        """Test for a background color with normal brightness."""
        background_color = 'rgb(150, 150, 150)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'normal')

    def test_high_red_component(self):
        """Test for a bright color with a high red component."""
        background_color = 'rgb(255, 100, 100)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'normal')

    def test_low_green_and_blue(self):
        """Test for a dark color with low green and blue components."""
        background_color = 'rgb(10, 10, 100)'
        result = is_background_too_dark_or_bright(background_color)
        self.assertEqual(result, 'dark')

if __name__ == '__main__':
    unittest.main()