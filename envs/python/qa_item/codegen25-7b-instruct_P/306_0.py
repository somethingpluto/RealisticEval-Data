d
e
f
 
g
e
t
_
p
r
i
c
e
(
r
e
c
i
p
e
_
i
d
:
 
s
t
r
,
 
m
i
n
_
v
a
l
:
 
f
l
o
a
t
 
=
 
1
0
,
 
m
a
x
_
v
a
l
:
 
f
l
o
a
t
 
=
 
3
0
)
 
-
>
 
f
l
o
a
t
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
r
e
c
i
p
e
 
I
D
 
i
s
 
h
a
s
h
e
d
 
t
o
 
p
r
o
d
u
c
e
 
a
 
p
r
i
c
e
 
i
n
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
r
a
n
g
e
.


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
r
e
c
i
p
e
_
i
d
 
(
s
t
r
)
:
 
T
h
e
 
I
D
 
o
f
 
t
h
e
 
r
e
c
i
p
e
 
t
o
 
h
a
s
h
.


 
 
 
 
 
 
 
 
m
i
n
_
v
a
l
 
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
 
m
i
n
i
m
u
m
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
i
c
e
 
r
a
n
g
e
 
(
d
e
f
a
u
l
t
 
i
s
 
1
0
)
.


 
 
 
 
 
 
 
 
m
a
x
_
v
a
l
 
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
 
m
a
x
i
m
u
m
 
v
a
l
u
e
 
o
f
 
t
h
e
 
p
r
i
c
e
 
r
a
n
g
e
 
(
d
e
f
a
u
l
t
 
i
s
 
3
0
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


 
 
 
 
 
 
 
 
f
l
o
a
t
:
 
T
h
e
 
h
a
s
h
e
d
 
p
r
i
c
e
,
 
m
a
p
p
e
d
 
t
o
 
t
h
e
 
s
p
e
c
i
f
i
e
d
 
r
a
n
g
e
 
w
i
t
h
 
t
w
o
 
d
e
c
i
m
a
l
 
p
l
a
c
e
s
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
 
r
o
u
n
d
(
m
i
n
_
v
a
l
 
+
 
(
m
a
x
_
v
a
l
 
-
 
m
i
n
_
v
a
l
)
 
*
 
f
l
o
a
t
(
h
a
s
h
l
i
b
.
s
h
a
2
5
6
(
r
e
c
i
p
e
_
i
d
.
e
n
c
o
d
e
(
)
)
.
h
e
x
d
i
g
e
s
t
(
)
)
 
/
 
0
x
f
f
f
f
f
f
f
f
,
 
2
)






d
e
f
 
g
e
t
_
i
n
g
r
e
d
i
e
n
t
s
(
r
e
c
i
p
e
_
i
d
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
s
t
r
]
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
r
e
c
i
p
e
 
I
D
 
i
s
 
h
a
s
h
e
d
 
t
o
 
p
r
o
d
u
c
e
 
a
 
l
i
s
t
 
o
f
 
i
n
g
r
e
d
i
e
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
i
p
e
_
i
d
 
(
s
t
r
)
:
 
T
h
e
 
I
D
 
o
f
 
t
h
e
 
r
e
c
i
p
e
 
t
o
 
h
a
s
h
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
[
s
t
r
]
:
 
T
h
e
 
l
i
s
t
 
o
f
 
i
n
g
r
e
d
i
e
n
t
s
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
 
[
s
t
r
(
i
)
 
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
r
e
c
i
p
e
_
i
d
)
)
]






d
e
f
 
g
e
t
_
i
n
g
r
e
d
i
e
n
t
_
w
e
i
g
h
t
s
(
r
e
c
i
p
e
_
i
d
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
f
l
o
a
t
]
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
r
e
c
i
p
e
 
I
D
 
i
s
 
h
a
s
h
e
d
 
t
o
 
p
r
o
d
u
c
e
 
a
 
l
i
s
t
 
o
f
 
i
n
g
r
e
d
i
e
n
t
 
w
e
i
g
h
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
i
p
e
_
i
d
 
(
s
t
r
)
:
 
T
h
e
 
I
D
 
o
f
 
t
h
e
 
r
e
c
i
p
e
 
t
o
 
h
a
s
h
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
[
f
l
o
a
t
]
:
 
T
h
e
 
l
i
s
t
 
o
f
 
i
n
g
r
e
d
i
e
n
t
 
w
e
i
g
h
t
s
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
 
[
f
l
o
a
t
(
i
)
 
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
r
e
c
i
p
e
_
i
d
)
)
]






d
e
f
 
g
e
t
_
i
n
g
r
e
d
i
e
n
t
_
p
r
i
c
e
s
(
r
e
c
i
p
e
_
i
d
:
 
s
t
r
)
 
-
>
 
L
i
s
t
[
f
l
o
a
t
]
:


 
 
 
 
"
"
"


 
 
 
 
T
h
e
 
r
e
c
i
p
e
 
I
D
 
i
s
 
h
a
s
h
e
d
 
t
o
 
p
r
o
d
u
c
e
 
a
 
l
i
s
t
 
o
f
 
i
n
g
r
e
d
i
e
n
t
 
p
r
i
c
e
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
i
p
e
_
i
d
 
(
s
t
r
)
:
 
T
h
e
 
I
D
 
o
f
 
t
h
e
 
r
e
c
i
p
e
 
t
o
 
h
a
s
h
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
[
f
l
o
a
t
]
:
 
T
h
e
 
l
i
s
t
 
o
f
 
i
n
g
r
e
d
i
e
n
t
 
p
r
i
c
e
s
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
 
[
g
e
t
_
p
r
i
c
e
(
r
e
c
i
p
e
_
i
d
,
 
m
i
n
_
v
a
l
=
1
0
,
 
m
a
x
_
v
a
l
=
3
0
)
 
f
o
r
 
_
 
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
r
e
c
i
p
e
_
i
d
)
)
]






d
e
f
 
g
e
t
import unittest


class TestGetPrice(unittest.TestCase):

    def test_default_range(self):
        price = get_price('recipe123')
        self.assertGreaterEqual(price, 10)
        self.assertLessEqual(price, 30)

    def test_same_price_for_same_id(self):
        price1 = get_price('recipe123')
        price2 = get_price('recipe123')
        self.assertEqual(price1, price2)

    def test_different_prices_for_different_ids(self):
        price1 = get_price('recipe123')
        price2 = get_price('recipe456')
        self.assertNotEqual(price1, price2)

    def test_custom_range(self):
        min_val = 20
        max_val = 50
        price = get_price('recipe789', min_val, max_val)
        self.assertGreaterEqual(price, min_val)
        self.assertLessEqual(price, max_val)

    def test_long_recipe_id(self):
        long_recipe_id = 'recipe' + 'A' * 1000
        price = get_price(long_recipe_id)
        self.assertGreaterEqual(price, 10)
        self.assertLessEqual(price, 30)

if __name__ == '__main__':
    unittest.main()