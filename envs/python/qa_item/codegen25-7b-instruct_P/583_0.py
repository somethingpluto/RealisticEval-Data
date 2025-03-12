d
e
f
 
r
e
m
o
v
e
_
q
u
e
r
y
_
p
a
r
a
m
(
u
r
l
:
 
s
t
r
,
 
k
e
y
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


 
 
 
 
R
e
m
o
v
e
s
 
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
 
p
a
r
a
m
e
t
e
r
 
f
r
o
m
 
t
h
e
 
U
R
L
 
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




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
p
a
r
s
e
s
 
t
h
e
 
U
R
L
,
 
r
e
m
o
v
e
s
 
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
 
q
u
e
r
y
 
p
a
r
a
m
e
t
e
r
,


 
 
 
 
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
 
t
h
e
 
m
o
d
i
f
i
e
d
 
U
R
L
.
 
I
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
 
d
o
e
s
 
n
o
t
 
e
x
i
s
t
,


 
 
 
 
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
 
U
R
L
 
i
s
 
r
e
t
u
r
n
e
d
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
 
'
h
t
t
p
:
/
/
e
x
a
m
p
l
e
.
c
o
m
/
p
a
g
e
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
'
,
 
'
s
e
a
r
c
h
'


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
'
h
t
t
p
:
/
/
e
x
a
m
p
l
e
.
c
o
m
/
p
a
g
e
?
p
a
g
e
=
1
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
f
r
o
m
 
w
h
i
c
h
 
t
o
 
r
e
m
o
v
e
 
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
.


 
 
 
 
 
 
 
 
k
e
y
 
(
s
t
r
)
:
 
T
h
e
 
k
e
y
 
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
 
t
o
 
r
e
m
o
v
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
 
m
o
d
i
f
i
e
d
 
U
R
L
 
w
i
t
h
 
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
 
p
a
r
a
m
e
t
e
r
 
r
e
m
o
v
e
d
.


 
 
 
 
"
"
"


 
 
 
 
p
a
r
s
e
d
_
u
r
l
 
=
 
u
r
l
p
a
r
s
e
(
u
r
l
)


 
 
 
 
q
u
e
r
y
_
p
a
r
a
m
s
 
=
 
p
a
r
s
e
_
q
s
(
p
a
r
s
e
d
_
u
r
l
.
q
u
e
r
y
)


 
 
 
 
i
f
 
k
e
y
 
i
n
 
q
u
e
r
y
_
p
a
r
a
m
s
:


 
 
 
 
 
 
 
 
q
u
e
r
y
_
p
a
r
a
m
s
.
p
o
p
(
k
e
y
)


 
 
 
 
 
 
 
 
n
e
w
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
 
=
 
u
r
l
e
n
c
o
d
e
(
q
u
e
r
y
_
p
a
r
a
m
s
,
 
d
o
s
e
q
=
T
r
u
e
)


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
u
r
l
u
n
p
a
r
s
e
(


 
 
 
 
 
 
 
 
 
 
 
 
(


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
s
e
d
_
u
r
l
.
s
c
h
e
m
e
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
s
e
d
_
u
r
l
.
n
e
t
l
o
c
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
s
e
d
_
u
r
l
.
p
a
t
h
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
s
e
d
_
u
r
l
.
p
a
r
a
m
s
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
n
e
w
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
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
s
e
d
_
u
r
l
.
f
r
a
g
m
e
n
t
,


 
 
 
 
 
 
 
 
 
 
 
 
)


 
 
 
 
 
 
 
 
)


 
 
 
 
r
e
t
u
r
n
 
u
r
l






d
e
f
 
a
d
d
_
q
u
e
r
y
_
p
a
r
a
m
(
u
r
l
:
 
s
t
r
,
 
k
e
y
:
 
s
t
r
,
 
v
a
l
u
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


 
 
 
 
A
d
d
s
 
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
 
p
a
r
a
m
e
t
e
r
 
t
o
 
t
h
e
 
U
R
L
 
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




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
p
a
r
s
e
s
 
t
h
e
 
U
R
L
,
 
a
d
d
s
 
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
 
q
u
e
r
y
 
p
a
r
a
m
e
t
e
r
,


 
 
 
 
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
 
t
h
e
 
m
o
d
i
f
i
e
d
 
U
R
L
.
 
I
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
 
a
l
r
e
a
d
y
 
e
x
i
s
t
s
,


 
 
 
 
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
 
U
R
L
 
i
s
 
r
e
t
u
r
n
e
d
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
 
'
h
t
t
p
:
/
/
e
x
a
m
p
l
e
.
c
o
m
/
p
a
g
e
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
'
,
 
'
s
e
a
r
c
h
'
,
 
'
t
e
s
t
2
'


 
 
 
 
 
 
 
 
-
 
O
u
t
p
u
t
:
 
'
h
t
t
p
:
/
/
e
x
a
m
p
l
e
.
c
o
m
/
p
a
g
e
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
'




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
u
r
l
 
(
s
t
r
)
:
 
T
h
e
 
U
R
L
 
t
o
 
w
h
i
c
h
 
t
o
 
a
d
d
 
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
.


 
 
 
 
 
 
 
 
k
e
y
 
(
s
t
r
)
:
 
T
h
e
 
k
e
y
 
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
 
t
o
 
a
d
d
.


 
 
 
 
 
 
 
 
v
a
l
u
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
a
r
a
m
e
t
e
r
 
t
o
 
a
d
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
 
m
o
d
i
f
i
e
d
 
U
R
L
 
w
i
t
h
import unittest


class TestRemoveQueryParam(unittest.TestCase):

    def test_remove_existing_parameter(self):
        url = 'https://example.com?page=1&sort=asc&filter=red'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/?page=1&filter=red')

    def test_no_modification_if_parameter_does_not_exist(self):
        url = 'https://example.com?page=1&filter=red'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/?page=1&filter=red')

    def test_return_original_url_if_no_query_parameters(self):
        url = 'https://example.com'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/')

    def test_remove_multiple_occurrences_of_a_parameter(self):
        url = 'https://example.com?page=1&filter=red&filter=blue'
        result = remove_query_param(url, 'filter')
        self.assertEqual(result, 'https://example.com/?page=1')

    def test_handle_encoded_characters_in_parameter(self):
        url = 'https://example.com?page=1&sort=asc&filter=hello%20world'
        result = remove_query_param(url, 'filter')
        self.assertEqual(result, 'https://example.com/?page=1&sort=asc')

    def test_handle_case_when_parameter_is_only_one_in_url(self):
        url = 'https://example.com?sort=asc'
        result = remove_query_param(url, 'sort')
        self.assertEqual(result, 'https://example.com/')

if __name__ == '__main__':
    unittest.main()