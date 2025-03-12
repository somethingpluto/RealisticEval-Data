d
e
f
 
t
o
_
q
u
e
r
y
_
s
t
r
i
n
g
(
p
a
r
a
m
s
:
 
d
i
c
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
a
 
q
u
e
r
y
 
s
t
r
i
n
g
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
 
{
'
s
e
a
r
c
h
'
:
 
'
t
e
s
t
'
,
 
'
p
a
g
e
'
:
 
1
,
 
'
s
i
z
e
'
:
 
1
0
}


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
'
?
s
e
a
r
c
h
=
t
e
s
t
&
p
a
g
e
=
1
&
s
i
z
e
=
1
0
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
r
a
m
s
 
(
d
i
c
t
)
:
 
T
h
e
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
c
o
n
v
e
r
t
.
 
T
h
e
 
k
e
y
s
 
s
h
o
u
l
d
 
b
e
 
s
t
r
i
n
g
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
v
a
l
u
e
s
 
c
a
n
 
b
e
 
o
f
 
a
n
y
 
t
y
p
e
 
t
h
a
t
 
c
a
n
 
b
e
 
c
o
n
v
e
r
t
e
d
 
t
o
 
a
 
s
t
r
i
n
g
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
 
q
u
e
r
y
 
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
 
p
a
r
a
m
e
t
e
r
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
 
'
?
'
 
+
 
'
&
'
.
j
o
i
n
(
f
'
{
k
}
=
{
v
}
'
 
f
o
r
 
k
,
 
v
 
i
n
 
p
a
r
a
m
s
.
i
t
e
m
s
(
)
)






d
e
f
 
t
o
_
q
u
e
r
y
_
s
t
r
i
n
g
_
l
i
s
t
(
p
a
r
a
m
s
:
 
d
i
c
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
a
 
q
u
e
r
y
 
s
t
r
i
n
g
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
 
{
'
s
e
a
r
c
h
'
:
 
[
'
t
e
s
t
'
,
 
'
t
e
s
t
2
'
]
,
 
'
p
a
g
e
'
:
 
1
,
 
'
s
i
z
e
'
:
 
1
0
}


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
'
?
s
e
a
r
c
h
=
t
e
s
t
&
s
e
a
r
c
h
=
t
e
s
t
2
&
p
a
g
e
=
1
&
s
i
z
e
=
1
0
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
r
a
m
s
 
(
d
i
c
t
)
:
 
T
h
e
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
c
o
n
v
e
r
t
.
 
T
h
e
 
k
e
y
s
 
s
h
o
u
l
d
 
b
e
 
s
t
r
i
n
g
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
v
a
l
u
e
s
 
s
h
o
u
l
d
 
b
e
 
l
i
s
t
s
 
o
f
 
s
t
r
i
n
g
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
 
T
h
e
 
q
u
e
r
y
 
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
 
p
a
r
a
m
e
t
e
r
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
 
'
?
'
 
+
 
'
&
'
.
j
o
i
n
(
f
'
{
k
}
=
{
v
}
'
 
f
o
r
 
k
,
 
v
 
i
n
 
p
a
r
a
m
s
.
i
t
e
m
s
(
)
 
f
o
r
 
v
 
i
n
 
v
)






d
e
f
 
t
o
_
q
u
e
r
y
_
s
t
r
i
n
g
_
l
i
s
t
_
v
a
l
u
e
s
(
p
a
r
a
m
s
:
 
d
i
c
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


 
 
 
 
C
o
n
v
e
r
t
s
 
a
 
d
i
c
t
i
o
n
a
r
y
 
o
f
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
a
 
q
u
e
r
y
 
s
t
r
i
n
g
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
 
{
'
s
e
a
r
c
h
'
:
 
[
'
t
e
s
t
'
,
 
'
t
e
s
t
2
'
]
,
 
'
p
a
g
e
'
:
 
1
,
 
'
s
i
z
e
'
:
 
1
0
}


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
'
?
s
e
a
r
c
h
=
t
e
s
t
&
s
e
a
r
c
h
=
t
e
s
t
2
&
p
a
g
e
=
1
&
s
i
z
e
=
1
0
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
p
a
r
a
m
s
 
(
d
i
c
t
)
:
 
T
h
e
 
p
a
r
a
m
e
t
e
r
s
 
t
o
 
c
o
n
v
e
r
t
.
 
T
h
e
 
k
e
y
s
 
s
h
o
u
l
d
 
b
e
 
s
t
r
i
n
g
s


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
n
d
 
v
a
l
u
e
s
 
s
h
o
u
l
d
 
b
e
 
l
i
s
t
s
 
o
f
 
s
t
r
i
n
g
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
 
T
h
e
 
q
u
e
r
y
 
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
 
p
a
r
a
m
e
t
e
r
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
 
'
?
'
 
+
 
'
&
'
.
j
o
i
n
(
f
'
{
k
}
=
{
v
}
'
 
f
o
r
 
k
,
 
v
 
i
n
 
p
a
r
a
m
s
.
i
t
e
m
s
(
)
 
f
o
r
 
v
 
i
n
 
v
)
import unittest


class TestToQueryString(unittest.TestCase):

    def test_convert_simple_object_to_query_string(self):
        params = {'search': 'test', 'page': 1, 'size': 10}
        result = to_query_string(params)
        self.assertEqual(result, '?search=test&page=1&size=10')

    def test_encode_special_characters_in_query_string(self):
        params = {'search': 'hello world', 'filter': 'price < \$50'}
        result = to_query_string(params)
        self.assertEqual(result, '?search=hello%20world&filter=price%20%3C%20%2450')

    def test_handle_empty_string_values(self):
        params = {'search': '', 'page': 1}
        result = to_query_string(params)
        self.assertEqual(result, '?search=&page=1')

    def test_handle_boolean_values(self):
        params = {'isActive': True, 'isVerified': False}
        result = to_query_string(params)
        self.assertEqual(result, '?isActive=True&isVerified=False')


if __name__ == '__main__':
    unittest.main()