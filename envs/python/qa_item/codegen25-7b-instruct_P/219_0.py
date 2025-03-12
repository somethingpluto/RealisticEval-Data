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
 
L
i
s
t






d
e
f
 
c
h
e
c
k
_
d
i
v
i
d
e
n
d
_
v
a
r
i
a
n
c
e
s
(
r
e
c
o
r
d
s
:
 
L
i
s
t
)
 
-
>
 
L
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
 
f
o
r
 
t
i
c
k
e
r
 
s
y
m
b
o
l
s
 
w
i
t
h
 
t
h
e
 
s
a
m
e
 
e
x
-
d
i
v
i
d
e
n
d
 
d
a
t
e
 
b
u
t
 
d
i
f
f
e
r
e
n
t
 
d
i
v
i
d
e
n
d
 
a
m
o
u
n
t
s
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
e
c
o
r
d
s
 
(
L
i
s
t
)
:
 
E
a
c
h
 
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
s
 
(
t
i
c
k
e
r
,
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
,
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
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


 
 
 
 
 
 
 
 
L
i
s
t
:
 
E
a
c
h
 
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
s
 
(
t
i
c
k
e
r
,
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
)
 
t
h
a
t
 
h
a
v
e
 
d
i
f
f
e
r
e
n
t
 
d
i
v
i
d
e
n
d
 
a
m
o
u
n
t
s
.


 
 
 
 
"
"
"


 
 
 
 
t
i
c
k
e
r
s
 
=
 
s
e
t
(
)


 
 
 
 
f
o
r
 
r
e
c
o
r
d
 
i
n
 
r
e
c
o
r
d
s
:


 
 
 
 
 
 
 
 
t
i
c
k
e
r
,
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
,
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
 
=
 
r
e
c
o
r
d


 
 
 
 
 
 
 
 
t
i
c
k
e
r
s
.
a
d
d
(
t
i
c
k
e
r
)


 
 
 
 
t
i
c
k
e
r
s
 
=
 
l
i
s
t
(
t
i
c
k
e
r
s
)




 
 
 
 
t
i
c
k
e
r
_
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
 
=
 
{
}


 
 
 
 
f
o
r
 
t
i
c
k
e
r
 
i
n
 
t
i
c
k
e
r
s
:


 
 
 
 
 
 
 
 
t
i
c
k
e
r
_
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
[
t
i
c
k
e
r
]
 
=
 
[
]


 
 
 
 
f
o
r
 
r
e
c
o
r
d
 
i
n
 
r
e
c
o
r
d
s
:


 
 
 
 
 
 
 
 
t
i
c
k
e
r
,
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
,
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
 
=
 
r
e
c
o
r
d


 
 
 
 
 
 
 
 
t
i
c
k
e
r
_
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
[
t
i
c
k
e
r
]
.
a
p
p
e
n
d
(
(
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
,
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
)
)




 
 
 
 
t
i
c
k
e
r
_
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
_
w
i
t
h
_
d
i
f
f
e
r
e
n
t
_
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
s
 
=
 
[
]


 
 
 
 
f
o
r
 
t
i
c
k
e
r
,
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
 
i
n
 
t
i
c
k
e
r
_
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
.
i
t
e
m
s
(
)
:


 
 
 
 
 
 
 
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
.
s
o
r
t
(
k
e
y
=
l
a
m
b
d
a
 
x
:
 
x
[
0
]
)


 
 
 
 
 
 
 
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
_
w
i
t
h
_
d
i
f
f
e
r
e
n
t
_
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
s
 
=
 
[
]


 
 
 
 
 
 
 
 
f
o
r
 
i
 
i
n
 
r
a
n
g
e
(
l
e
n
(
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
)
 
-
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
_
1
,
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
_
1
 
=
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
[
i
]


 
 
 
 
 
 
 
 
 
 
 
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
_
2
,
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
_
2
 
=
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
[
i
 
+
 
1
]


 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
_
1
 
!
=
 
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
_
2
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
_
w
i
t
h
_
d
i
f
f
e
r
e
n
t
_
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
s
.
a
p
p
e
n
d
(
(
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
_
1
,
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
_
2
)
)


 
 
 
 
 
 
 
 
i
f
 
e
x
_
d
i
v
i
d
e
n
d
_
d
a
t
e
s
_
w
i
t
h
_
d
i
f
f
e
r
e
n
t
_
d
i
v
i
d
e
n
d
_
a
m
o
u
n
t
s
:
import unittest


class TestCheckDividendVariances(unittest.TestCase):

    def test_no_inconsistencies(self):
        records = [
            ('AAPL', '2023-09-01', 0.22),
            ('AAPL', '2023-09-01', 0.22),
            ('MSFT', '2023-09-01', 0.56),
            ('GOOG', '2023-09-02', 0.00)
        ]
        expected_output = []
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_one_inconsistency(self):
        records = [
            ('AAPL', '2023-09-01', 0.22),
            ('AAPL', '2023-09-01', 0.23),  # Different amount
            ('MSFT', '2023-09-01', 0.56),
            ('GOOG', '2023-09-02', 0.00)
        ]
        expected_output = [('AAPL', '2023-09-01')]
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_multiple_inconsistencies(self):
        records = [
            ('AAPL', '2023-09-01', 0.22),
            ('AAPL', '2023-09-01', 0.23),  # Different amount
            ('MSFT', '2023-09-01', 0.56),
            ('MSFT', '2023-09-01', 0.60),  # Different amount
            ('GOOG', '2023-09-02', 0.00),
            ('TSLA', '2023-09-03', 0.10),
            ('TSLA', '2023-09-03', 0.10),  # Same amount, no inconsistency
            ('TSLA', '2023-09-03', 0.15)  # Different amount
        ]
        expected_output = [('AAPL', '2023-09-01'), ('MSFT', '2023-09-01'), ('TSLA', '2023-09-03')]
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_single_record(self):
        records = [
            ('AAPL', '2023-09-01', 0.22)
        ]
        expected_output = []
        self.assertEqual(check_dividend_variances(records), expected_output)

    def test_empty_list(self):
        records = []
        expected_output = []
        self.assertEqual(check_dividend_variances(records), expected_output)

if __name__ == '__main__':
    unittest.main()