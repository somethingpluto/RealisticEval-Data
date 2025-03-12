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
 
D
i
c
t






d
e
f
 
c
l
e
a
n
_
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
(
i
n
p
u
t
_
d
i
c
t
:
D
i
c
t
)
 
-
>
 
D
i
c
t
:


 
 
 
 
"
"
"


 
 
 
 
C
l
e
a
n
s
 
t
h
e
 
i
n
p
u
t
 
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
 
b
y
 
r
e
m
o
v
i
n
g
 
k
e
y
s
 
w
i
t
h
 
i
n
v
a
l
i
d
 
v
a
l
u
e
s
.
V
a
l
i
d
 
v
a
l
u
e
s
 
a
r
e
 
n
o
n
-
N
a
N
,
 
n
o
n
-
N
o
n
e
,
 
a
n
d
 
n
o
n
-
w
h
i
t
e
s
p
a
c
e
 
s
t
r
i
n
g
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
d
i
c
t
 
(
D
i
c
t
)
:
 
A
 
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
 
t
o
 
b
e
 
c
l
e
a
n
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


 
 
 
 
 
 
 
 
D
i
c
t
:
 
A
 
n
e
w
 
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
 
o
n
l
y
 
v
a
l
i
d
 
v
a
l
u
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
 
{
k
:
v
 
f
o
r
 
k
,
v
 
i
n
 
i
n
p
u
t
_
d
i
c
t
.
i
t
e
m
s
(
)
 
i
f
 
i
s
_
v
a
l
i
d
_
v
a
l
u
e
(
v
)
}




d
e
f
 
i
s
_
v
a
l
i
d
_
v
a
l
u
e
(
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
 
b
o
o
l
:


 
 
 
 
"
"
"


 
 
 
 
C
h
e
c
k
s
 
i
f
 
a
 
v
a
l
u
e
 
i
s
 
v
a
l
i
d
.
 
V
a
l
i
d
 
v
a
l
u
e
s
 
a
r
e
 
n
o
n
-
N
a
N
,
 
n
o
n
-
N
o
n
e
,
 
a
n
d
 
n
o
n
-
w
h
i
t
e
s
p
a
c
e
 
s
t
r
i
n
g
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
A
 
v
a
l
u
e
 
t
o
 
b
e
 
c
h
e
c
k
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


 
 
 
 
 
 
 
 
b
o
o
l
:
 
T
r
u
e
 
i
f
 
t
h
e
 
v
a
l
u
e
 
i
s
 
v
a
l
i
d
,
 
F
a
l
s
e
 
o
t
h
e
r
w
i
s
e
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
 
v
a
l
u
e
 
i
s
 
n
o
t
 
N
o
n
e
 
a
n
d
 
v
a
l
u
e
 
!
=
 
'
'
 
a
n
d
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
v
a
l
u
e
,
 
f
l
o
a
t
)
 
a
n
d
 
n
o
t
 
i
s
i
n
s
t
a
n
c
e
(
v
a
l
u
e
,
 
i
n
t
)




d
e
f
 
g
e
t
_
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
_
v
a
l
u
e
(
i
n
p
u
t
_
d
i
c
t
:
D
i
c
t
,
 
k
e
y
:
s
t
r
,
 
d
e
f
a
u
l
t
_
v
a
l
u
e
:
s
t
r
=
N
o
n
e
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
t
s
 
a
 
v
a
l
u
e
 
f
r
o
m
 
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
.
 
I
f
 
t
h
e
 
k
e
y
 
i
s
 
n
o
t
 
f
o
u
n
d
,
 
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
 
d
e
f
a
u
l
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
d
i
c
t
 
(
D
i
c
t
)
:
 
A
 
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
 
t
o
 
g
e
t
 
a
 
v
a
l
u
e
 
f
r
o
m
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
 
A
 
k
e
y
 
t
o
 
g
e
t
 
a
 
v
a
l
u
e
 
f
r
o
m
.


 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
_
v
a
l
u
e
 
(
s
t
r
,
 
o
p
t
i
o
n
a
l
)
:
 
A
 
d
e
f
a
u
l
t
 
v
a
l
u
e
 
t
o
 
r
e
t
u
r
n
 
i
f
 
t
h
e
 
k
e
y
 
i
s
 
n
o
t
 
f
o
u
n
d
.
 
D
e
f
a
u
l
t
s
 
t
o
 
N
o
n
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
 
A
 
v
a
l
u
e
 
f
r
o
m
 
t
h
e
 
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
r
 
t
h
e
 
d
e
f
a
u
l
t
 
v
a
l
u
e
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
 
i
n
p
u
t
_
d
i
c
t
.
g
e
t
(
k
e
y
,
 
d
e
f
a
u
l
t
_
v
a
l
u
e
)




d
e
f
 
g
e
t
_
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
_
v
a
l
u
e
s
(
i
n
p
u
t
_
d
i
c
t
:
D
i
c
t
,
 
k
e
y
s
:
l
i
s
t
,
 
d
e
f
a
u
l
t
_
v
a
l
u
e
:
s
t
r
=
N
o
n
e
)
 
-
>
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
v
a
l
u
e
s
 
f
r
o
m
 
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
.
 
I
f
 
t
h
e
 
k
e
y
 
i
s
 
n
o
t
 
f
o
u
n
d
,
 
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
 
d
e
f
a
u
l
t
 
v
a
l
u
e
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
i
n
p
u
t
_
d
i
c
t
 
(
D
i
c
t
)
:
 
A
 
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
 
t
o
 
g
e
t
 
v
a
l
u
e
s
 
f
r
o
m
.


 
 
 
 
 
 
 
 
k
e
y
s
 
(
l
i
s
t
)
:
 
A
 
l
i
s
t
 
o
f
 
k
e
y
s
 
t
o
 
g
e
t
 
v
a
l
u
e
s
 
f
r
o
m
.


 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
_
v
a
l
u
e
 
(
s
t
r
,
 
o
p
t
i
o
n
a
l
)
:
 
A
 
d
e
f
a
u
l
t
 
v
a
l
u
e
 
t
o
 
r
e
t
u
r
n
 
i
f
 
t
h
e
 
k
e
y
 
i
s
 
n
o
t
 
f
o
u
n
d
.
 
D
e
f
import unittest

import numpy as np


class TestCleanDictionary(unittest.TestCase):

    def test_valid_strings(self):
        """ Test a dictionary with valid strings. """
        input_dict = {
            'key1': 'valid string',
            'key2': 'another valid string'
        }
        expected_output = {
            'key1': 'valid string',
            'key2': 'another valid string'
        }
        self.assertEqual(clean_dictionary(input_dict), expected_output)

    def test_none_and(self):
        """ Test a dictionary with None and NaN values. """
        input_dict = {
            'key1': None,
            'key3': 'valid string'
        }
        expected_output = {
            'key3': 'valid string'
        }
        self.assertEqual(clean_dictionary(input_dict), expected_output)

    def test_whitespace_strings(self):
        """ Test a dictionary with whitespace strings. """
        input_dict = {
            'key1': '   ',
            'key2': '',
            'key3': 'valid'
        }
        expected_output = {
            'key3': 'valid'
        }
        self.assertEqual(clean_dictionary(input_dict), expected_output)

    def test_empty_dictionary(self):
        """ Test an empty dictionary. """
        input_dict = {}
        expected_output = {}
        self.assertEqual(clean_dictionary(input_dict), expected_output)

if __name__ == '__main__':
    unittest.main()