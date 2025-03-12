d
e
f
 
g
e
n
e
r
a
t
e
_
d
a
t
e
_
r
a
n
g
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
a
r
t
_
d
a
t
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
d
a
t
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
n
e
r
a
t
e
s
 
a
 
s
t
r
i
n
g
 
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
 
e
n
t
e
r
e
d
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
d
a
t
e
s
.
 
I
f
 
t
h
e
 
s
t
a
r
t
 
d
a
t
e
 
a
n
d
 
e
n
d
 
d
a
t
e
 
a
r
e
 
i
n
 
t
h
e
 
s
a
m
e
 
m
o
n
t
h
,
 
o
n
l
y
 
o
n
e
 
m
o
n
t
h
 
w
i
l
l
 
b
e
 
d
i
s
p
l
a
y
e
d
.
 
I
f
 
n
o
t
,
 
t
h
e
 
s
t
a
r
t
 
a
n
d
 
e
n
d
 
m
o
n
t
h
s
 
w
i
l
l
 
b
e
 
d
i
s
p
l
a
y
e
d
 
s
e
p
a
r
a
t
e
l
y
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
,
 
i
f
 
y
o
u
 
e
n
t
e
r
 
t
h
e
 
s
t
a
r
t
 
d
a
t
e
 
a
n
d
 
e
n
d
 
d
a
t
e
 
a
s
,
"
2
0
2
3
-
0
8
-
0
1
"
 
a
n
d
 
"
2
0
2
3
-
0
8
-
1
5
"
 
r
e
s
p
e
c
t
i
v
e
l
y
,
 
y
o
u
 
w
i
l
l
 
f
i
n
a
l
l
y
 
o
u
t
p
u
t
 
"
A
u
g
u
s
t
 
1
 
t
o
 
1
5
,
 
2
0
2
3
"
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


 
 
 
 
 
 
 
 
i
n
p
u
t
:


 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
r
t
_
d
a
t
e
:
 
2
0
2
3
-
0
8
-
0
1


 
 
 
 
 
 
 
 
 
 
 
 
e
n
d
_
d
a
t
e
:
 
2
0
2
3
-
0
8
-
1
5


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:


 
 
 
 
 
 
 
 
 
 
 
 
A
u
g
u
s
t
 
1
 
t
o
 
1
5
,
 
2
0
2
3




 
 
 
 
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
d
a
t
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
 
d
a
t
e
 
i
n
 
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
d
a
t
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
 
d
a
t
e
 
i
n
 
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
 
A
 
s
t
r
i
n
g
 
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
 
d
a
t
e
 
r
a
n
g
e
 
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
d
a
t
e
_
o
b
j
 
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
d
a
t
e
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
n
d
_
d
a
t
e
_
o
b
j
 
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
d
a
t
e
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




 
 
 
 
i
f
 
s
t
a
r
t
_
d
a
t
e
_
o
b
j
.
m
o
n
t
h
 
=
=
 
e
n
d
_
d
a
t
e
_
o
b
j
.
m
o
n
t
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
s
t
a
r
t
_
d
a
t
e
_
o
b
j
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
'
%
B
'
)
}
 
{
s
t
a
r
t
_
d
a
t
e
_
o
b
j
.
d
a
y
}
,
 
{
s
t
a
r
t
_
d
a
t
e
_
o
b
j
.
y
e
a
r
}
 
t
o
 
{
e
n
d
_
d
a
t
e
_
o
b
j
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
'
%
B
'
)
}
 
{
e
n
d
_
d
a
t
e
_
o
b
j
.
d
a
y
}
,
 
{
e
n
d
_
d
a
t
e
_
o
b
j
.
y
e
a
r
}
"


 
 
 
 
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
 
f
"
{
s
t
a
r
t
_
d
a
t
e
_
o
b
j
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
'
%
B
'
)
}
 
{
s
t
a
r
t
_
d
a
t
e
_
o
b
j
.
d
a
y
}
,
 
{
s
t
a
r
t
_
d
a
t
e
_
o
b
j
.
y
e
a
r
}
 
t
o
 
{
e
n
d
_
d
a
t
e
_
o
b
j
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
'
%
B
'
)
}
 
{
e
n
d
_
d
a
t
e
_
o
b
j
.
d
a
y
}
,
 
{
e
n
d
_
d
a
t
e
_
o
b
j
.
y
e
a
r
}
"


import unittest


class TestDateRangeString(unittest.TestCase):
    def test_same_month(self):
        # Test dates within the same month
        result = generate_date_range_string("2023-08-01", "2023-08-15")
        self.assertEqual(result, "August 1 to 15, 2023")

    def test_same_month_star_end(self):
        # Test dates within the same month
        result = generate_date_range_string("2023-08-01", "2023-08-31")
        self.assertEqual(result, "August 1 to 31, 2023")

    def test_different_months_same_year(self):
        # Test dates across different months within the same year
        result = generate_date_range_string("2023-08-30", "2023-09-05")
        self.assertEqual(result, "August 30, 2023 to September 5, 2023")

    def test_different_years(self):
        # Test dates across different years
        result = generate_date_range_string("2023-12-30", "2024-01-02")
        self.assertEqual(result, "December 30, 2023 to January 2, 2024")

if __name__ == '__main__':
    unittest.main()