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
 
s
t
r
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
s
 
t
h
e
 
a
g
e
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
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
 
a
n
d
 
r
e
t
u
r
n
s
 
a
 
s
t
r
i
n
g
 
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
 
o
r
i
g
i
n
a
l
 
b
i
r
t
h
 
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
a
l
c
u
l
a
t
e
d
 
a
g
e
.
 
I
f
 
t
h
e
 
e
n
t
e
r
e
d
 
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
 
i
s
 
i
n
v
a
l
i
d


 
 
 
 
o
r
 
e
m
p
t
y
,
 
t
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
 
r
e
t
u
r
n
s
 
a
n
 
e
m
p
t
y
 
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
n
 
a
 
r
e
c
o
g
n
i
z
a
b
l
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


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
(
e
.
g
.
,
 
'
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
'
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
 
t
h
a
t
 
i
n
c
l
u
d
e
s
 
t
h
e
 
o
r
i
g
i
n
a
l
 
b
i
r
t
h
 
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
a
l
c
u
l
a
t
e
d
 
a
g
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
 
'
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
a
g
e
)
'
,
 
o
r
 
a
n
 
e
m
p
t
y
 
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
 
i
n
p
u
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


 
 
 
 
i
f
 
n
o
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
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
'
'




 
 
 
 
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
 
'
%
Y
-
%
m
-
%
d
'
)


 
 
 
 
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
 
'
'




 
 
 
 
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
n
o
w
(
)


 
 
 
 
a
g
e
 
=
 
n
o
w
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
n
o
w
.
m
o
n
t
h
,
 
n
o
w
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
 
f
'
{
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
}
 
(
{
a
g
e
}
 
y
e
a
r
s
 
o
l
d
)
'






d
e
f
 
m
a
i
n
(
)
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
 
=
 
i
n
p
u
t
(
'
E
n
t
e
r
 
y
o
u
r
 
b
i
r
t
h
 
d
a
t
e
 
(
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
)
:
 
'
)


 
 
 
 
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
)
)






i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
'
_
_
m
a
i
n
_
_
'
:


 
 
 
 
m
a
i
n
(
)


import unittest


class TestCalculateAge(unittest.TestCase):

    def test_birthday_today(self):
        self.assertEqual(calculate_age('2000-08-23'), '2000-08-23 (24)')

    def test_birthday_passed_this_year(self):
        self.assertEqual(calculate_age('1990-01-15'), '1990-01-15 (34)')

    def test_birthday_at_end_of_year(self):
        self.assertEqual(calculate_age('1985-12-31'), '1985-12-31 (38)')

    def test_recently_turned_one_year_old(self):
        self.assertEqual(calculate_age('2023-05-05'), '2023-05-05 (1)')

    def test_invalid_date_input(self):
        self.assertEqual(calculate_age('invalid-date'), '')

if __name__ == '__main__':
    unittest.main()