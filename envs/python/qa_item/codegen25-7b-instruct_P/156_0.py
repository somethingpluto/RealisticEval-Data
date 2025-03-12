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
n
u
m
b
e
r
(
n
u
m
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
 
t
h
e
 
n
u
m
b
e
r
 
i
n
t
o
 
a
 
m
o
r
e
 
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
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
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
 
f
o
r
m
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
i
s
 
l
e
s
s
 
t
h
a
n
 
1
,
0
0
0
.


 
 
 
 
I
f
 
i
t
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
a
 
t
h
o
u
s
a
n
d
 
a
n
d
 
l
e
s
s
 
t
h
a
n
 
a
 
m
i
l
l
i
o
n
,
 
i
t
 
i
s
 
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
 
"
x
.
x
K
"
.


 
 
 
 
F
o
r
 
a
 
m
i
l
l
i
o
n
 
o
r
 
m
o
r
e
,
 
f
o
r
m
a
t
 
i
t
 
a
s
 
"
x
.
x
M
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
 
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
 
n
u
m
b
e
r
 
t
o
 
b
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
 
f
o
r
m
a
t
t
e
d
 
n
u
m
b
e
r
 
a
s
 
a
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
u
m
 
<
 
1
0
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
n
u
m
)


 
 
 
 
e
l
i
f
 
n
u
m
 
<
 
1
0
0
0
0
0
0
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
n
u
m
/
1
0
0
0
:
.
1
f
}
K
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
n
u
m
/
1
0
0
0
0
0
0
:
.
1
f
}
M
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
e
r
c
e
n
t
a
g
e
(
n
u
m
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
 
t
h
e
 
n
u
m
b
e
r
 
i
n
t
o
 
a
 
m
o
r
e
 
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
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
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
 
f
o
r
m
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
i
s
 
l
e
s
s
 
t
h
a
n
 
1
,
0
0
0
.


 
 
 
 
I
f
 
i
t
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
a
 
t
h
o
u
s
a
n
d
 
a
n
d
 
l
e
s
s
 
t
h
a
n
 
a
 
m
i
l
l
i
o
n
,
 
i
t
 
i
s
 
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
 
"
x
.
x
K
"
.


 
 
 
 
F
o
r
 
a
 
m
i
l
l
i
o
n
 
o
r
 
m
o
r
e
,
 
f
o
r
m
a
t
 
i
t
 
a
s
 
"
x
.
x
M
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
 
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
 
n
u
m
b
e
r
 
t
o
 
b
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
 
f
o
r
m
a
t
t
e
d
 
n
u
m
b
e
r
 
a
s
 
a
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
u
m
 
<
 
1
0
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
n
u
m
)


 
 
 
 
e
l
i
f
 
n
u
m
 
<
 
1
0
0
0
0
0
0
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
n
u
m
/
1
0
0
0
:
.
1
f
}
K
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
n
u
m
/
1
0
0
0
0
0
0
:
.
1
f
}
M
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
c
u
r
r
e
n
c
y
(
n
u
m
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
 
t
h
e
 
n
u
m
b
e
r
 
i
n
t
o
 
a
 
m
o
r
e
 
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
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
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
 
f
o
r
m
 
i
f
 
t
h
e
 
n
u
m
b
e
r
 
i
s
 
l
e
s
s
 
t
h
a
n
 
1
,
0
0
0
.


 
 
 
 
I
f
 
i
t
 
i
s
 
g
r
e
a
t
e
r
 
t
h
a
n
 
o
r
 
e
q
u
a
l
 
t
o
 
a
 
t
h
o
u
s
a
n
d
 
a
n
d
 
l
e
s
s
 
t
h
a
n
 
a
 
m
i
l
l
i
o
n
,
 
i
t
 
i
s
 
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
 
"
x
.
x
K
"
.


 
 
 
 
F
o
r
 
a
 
m
i
l
l
i
o
n
 
o
r
 
m
o
r
e
,
 
f
o
r
m
a
t
 
i
t
 
a
s
 
"
x
.
x
M
"
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
 
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
 
n
u
m
b
e
r
 
t
o
 
b
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
 
f
o
r
m
a
t
t
e
d
 
n
u
m
b
e
r
 
a
s
 
a
 
s
t
r
i
n
g
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
u
m
 
<
 
1
0
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
n
u
m
)


 
 
 
 
e
l
i
f
 
n
u
m
 
<
 
1
0
0
0
0
0
0
:


import unittest


class TestFormatNumber(unittest.TestCase):
    def test_format_greater_than_equal_to_million(self):
        """should format numbers greater than or equal to 1,000,000 with 'M' suffix"""
        self.assertEqual(format_number(1500000), '1.5M')
        self.assertEqual(format_number(1000000), '1.0M')

    def test_format_greater_than_equal_to_thousand(self):
        """should format numbers greater than or equal to 1,000 but less than 1,000,000 with 'K' suffix"""
        self.assertEqual(format_number(2500), '2.5K')
        self.assertEqual(format_number(1000), '1.0K')

    def test_return_string_if_less_than_thousand(self):
        """should return the number as a string if it is less than 1,000"""
        self.assertEqual(format_number(999), '999')
        self.assertEqual(format_number(500), '500')

    def test_handle_edge_cases(self):
        """should handle edge cases like exactly 1,000 or 1,000,000"""
        self.assertEqual(format_number(1000), '1.0K')
        self.assertEqual(format_number(1000000), '1.0M')

if __name__ == '__main__':
    unittest.main()