d
e
f
 
a
b
b
r
e
v
i
a
t
e
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
b
e
r
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


 
 
 
 
A
b
b
r
e
v
i
a
t
e
s
 
a
 
n
u
m
b
e
r
 
t
o
 
a
 
s
t
r
i
n
g
 
w
i
t
h
 
a
 
s
u
f
f
i
x
 
b
a
s
e
d
 
o
n
 
i
t
s
 
m
a
g
n
i
t
u
d
e
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
 
u
s
e
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
u
f
f
i
x
e
s
 
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
 
n
u
m
b
e
r
'
s
 
m
a
g
n
i
t
u
d
e
:


 
 
 
 
-
 
"
"
 
(
n
o
 
s
u
f
f
i
x
)
 
f
o
r
 
v
a
l
u
e
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


 
 
 
 
-
 
"
k
"
 
f
o
r
 
t
h
o
u
s
a
n
d
s
 
(
1
,
0
0
0
)


 
 
 
 
-
 
"
M
"
 
f
o
r
 
m
i
l
l
i
o
n
s
 
(
1
,
0
0
0
,
0
0
0
)


 
 
 
 
-
 
"
B
"
 
f
o
r
 
b
i
l
l
i
o
n
s
 
(
1
,
0
0
0
,
0
0
0
,
0
0
0
)


 
 
 
 
-
 
"
T
"
 
f
o
r
 
t
r
i
l
l
i
o
n
s
 
(
1
,
0
0
0
,
0
0
0
,
0
0
0
,
0
0
0
)




 
 
 
 
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
 
9
9
9
 
 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
9
9
9
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
5
4
9
 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
.
5
k
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
0
0
0
 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
k
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
2
3
4
5
6
7
8
9
0
1
2
3
 
 
 
O
u
t
p
u
t
:
 
"
1
.
2
T
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
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
 
a
b
b
r
e
v
i
a
t
e
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
 
a
b
b
r
e
v
i
a
t
e
d
 
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
 
o
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
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
n
u
m
b
e
r
 
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
b
e
r
)




 
 
 
 
m
a
g
n
i
t
u
d
e
 
=
 
0


 
 
 
 
w
h
i
l
e
 
n
u
m
b
e
r
 
>
=
 
1
0
0
0
:


 
 
 
 
 
 
 
 
m
a
g
n
i
t
u
d
e
 
+
=
 
1


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
/
=
 
1
0
0
0
.
0




 
 
 
 
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
b
e
r
:
.
1
f
}
k
"






d
e
f
 
a
b
b
r
e
v
i
a
t
e
_
n
u
m
b
e
r
_
w
i
t
h
_
u
n
i
t
s
(
n
u
m
b
e
r
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


 
 
 
 
A
b
b
r
e
v
i
a
t
e
s
 
a
 
n
u
m
b
e
r
 
t
o
 
a
 
s
t
r
i
n
g
 
w
i
t
h
 
a
 
s
u
f
f
i
x
 
b
a
s
e
d
 
o
n
 
i
t
s
 
m
a
g
n
i
t
u
d
e
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
 
u
s
e
s
 
t
h
e
 
f
o
l
l
o
w
i
n
g
 
s
u
f
f
i
x
e
s
 
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
 
n
u
m
b
e
r
'
s
 
m
a
g
n
i
t
u
d
e
:


 
 
 
 
-
 
"
"
 
(
n
o
 
s
u
f
f
i
x
)
 
f
o
r
 
v
a
l
u
e
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


 
 
 
 
-
 
"
k
"
 
f
o
r
 
t
h
o
u
s
a
n
d
s
 
(
1
,
0
0
0
)


 
 
 
 
-
 
"
M
"
 
f
o
r
 
m
i
l
l
i
o
n
s
 
(
1
,
0
0
0
,
0
0
0
)


 
 
 
 
-
 
"
B
"
 
f
o
r
 
b
i
l
l
i
o
n
s
 
(
1
,
0
0
0
,
0
0
0
,
0
0
0
)


 
 
 
 
-
 
"
T
"
 
f
o
r
 
t
r
i
l
l
i
o
n
s
 
(
1
,
0
0
0
,
0
0
0
,
0
0
0
,
0
0
0
)




 
 
 
 
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
 
9
9
9
 
 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
9
9
9
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
5
4
9
 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
.
5
k
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
0
0
0
 
 
 
 
 
 
 
 
 
 
 
 
O
u
t
p
u
t
:
 
"
1
k
"


 
 
 
 
 
 
 
 
-
 
I
n
p
u
t
:
 
1
2
3
4
5
6
7
8
9
0
1
2
3
 
 
 
O
u
t
p
u
t
:
 
"
1
.
2
T
"




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
n
u
m
b
e
r
 
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
 
a
b
b
r
e
v
i
a
t
e
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
import unittest


class TestAbbreviateNumber(unittest.TestCase):

    def test_less_than_1000(self):
        # should return the same number for values less than 1000
        self.assertEqual(abbreviate_number(999), '999')

    def test_one_thousand(self):
        # should return "1k" for 1000
        result = abbreviate_number(1000)
        self.assertIn(result, ['1k', '1.0k'])

    def test_one_thousand_five_hundred(self):
        # should return "1.5k" for 1500
        self.assertEqual(abbreviate_number(1500), '1.5k')

    def test_one_million(self):
        # should return "1M" for 1 million
        result = abbreviate_number(1000000)
        self.assertIn(result, ['1M', '1.0M'])

    def test_twenty_five_million(self):
        # should return "25M" for 25 million
        self.assertEqual(abbreviate_number(25000000), '25M')

    def test_one_billion(self):
        # should return "1B" for 1 billion
        result = abbreviate_number(1000000000)
        self.assertIn(result, ['1B', '1.0B'])

    def test_one_point_two_trillion(self):
        # should return "1.2T" for 1.2 trillion
        self.assertEqual(abbreviate_number(1234567890123), '1.2T')

if __name__ == '__main__':
    unittest.main()