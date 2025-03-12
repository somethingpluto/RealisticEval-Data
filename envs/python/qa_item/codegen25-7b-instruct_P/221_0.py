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
,
 
L
i
s
t






d
e
f
 
e
x
t
r
a
c
t
_
p
a
r
s
e
_
d
i
c
t
s
(
f
i
l
e
_
p
a
t
h
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
D
i
c
t
]
:


 
 
 
 
"
"
"


 
 
 
 
e
x
t
r
a
c
t
 
a
n
d
 
p
a
r
s
e
 
s
t
r
i
n
g
s
 
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
 
P
y
t
h
o
n
 
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
 
s
y
n
t
a
x
 
f
r
o
m
 
a
 
g
i
v
e
n
 
f
i
l
e


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
f
i
l
e
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
f
i
l
e
 
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
 
e
x
t
r
a
c
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
 
e
x
t
r
a
c
t
e
d
 
a
n
d
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
f
i
l
e
.


 
 
 
 
"
"
"


 
 
 
 
w
i
t
h
 
o
p
e
n
(
f
i
l
e
_
p
a
t
h
,
 
"
r
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
l
i
n
e
s
 
=
 
f
.
r
e
a
d
l
i
n
e
s
(
)


 
 
 
 
p
a
r
s
e
_
d
i
c
t
s
 
=
 
[
]


 
 
 
 
f
o
r
 
l
i
n
e
 
i
n
 
l
i
n
e
s
:


 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
.
s
t
a
r
t
s
w
i
t
h
(
"
{
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
t
r
y
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
r
s
e
_
d
i
c
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
e
v
a
l
(
l
i
n
e
)
)


 
 
 
 
 
 
 
 
 
 
 
 
e
x
c
e
p
t
 
S
y
n
t
a
x
E
r
r
o
r
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
s
s


 
 
 
 
r
e
t
u
r
n
 
p
a
r
s
e
_
d
i
c
t
s






d
e
f
 
e
x
t
r
a
c
t
_
p
a
r
s
e
_
d
i
c
t
s
_
f
r
o
m
_
d
i
r
(
d
i
r
_
p
a
t
h
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
D
i
c
t
]
:


 
 
 
 
"
"
"


 
 
 
 
e
x
t
r
a
c
t
 
a
n
d
 
p
a
r
s
e
 
s
t
r
i
n
g
s
 
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
 
P
y
t
h
o
n
 
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
 
s
y
n
t
a
x
 
f
r
o
m
 
a
l
l
 
f
i
l
e
s
 
i
n
 
a
 
g
i
v
e
n
 
d
i
r
e
c
t
o
r
y


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
_
p
a
t
h
 
(
s
t
r
)
:
 
T
h
e
 
p
a
t
h
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
y
 
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
 
e
x
t
r
a
c
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
 
e
x
t
r
a
c
t
e
d
 
a
n
d
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
f
i
l
e
s
 
i
n
 
t
h
e
 
d
i
r
e
c
t
o
r
y
.


 
 
 
 
"
"
"


 
 
 
 
f
i
l
e
_
p
a
t
h
s
 
=
 
[


 
 
 
 
 
 
 
 
o
s
.
p
a
t
h
.
j
o
i
n
(
d
i
r
_
p
a
t
h
,
 
f
)


 
 
 
 
 
 
 
 
f
o
r
 
f
 
i
n
 
o
s
.
l
i
s
t
d
i
r
(
d
i
r
_
p
a
t
h
)


 
 
 
 
 
 
 
 
i
f
 
o
s
.
p
a
t
h
.
i
s
f
i
l
e
(
o
s
.
p
a
t
h
.
j
o
i
n
(
d
i
r
_
p
a
t
h
,
 
f
)
)


 
 
 
 
]


 
 
 
 
p
a
r
s
e
_
d
i
c
t
s
 
=
 
[
]


 
 
 
 
f
o
r
 
f
i
l
e
_
p
a
t
h
 
i
n
 
f
i
l
e
_
p
a
t
h
s
:


 
 
 
 
 
 
 
 
p
a
r
s
e
_
d
i
c
t
s
.
e
x
t
e
n
d
(
e
x
t
r
a
c
t
_
p
a
r
s
e
_
d
i
c
t
s
(
f
i
l
e
_
p
a
t
h
)
)


 
 
 
 
r
e
t
u
r
n
 
p
a
r
s
e
_
d
i
c
t
s






d
e
f
 
e
x
t
r
a
c
t
_
p
a
r
s
e
_
d
i
c
t
s
_
f
r
o
m
_
d
i
r
s
(
d
i
r
_
p
a
t
h
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
)
 
-
>
 
L
i
s
t
[
D
i
c
t
]
:


 
 
 
 
"
"
"


 
 
 
 
e
x
t
r
a
c
t
 
a
n
d
 
p
a
r
s
e
 
s
t
r
i
n
g
s
 
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
 
P
y
t
h
o
n
 
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
 
s
y
n
t
a
x
 
f
r
o
m
 
a
l
l
 
f
i
l
e
s
 
i
n
 
a
 
g
i
v
e
n
 
l
i
s
t
 
o
f
 
d
i
r
e
c
t
o
r
i
e
s


 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
i
r
_
p
a
t
h
s
 
(
l
i
s
t
)
:
 
T
h
e
 
p
a
t
h
s
 
t
o
 
t
h
e
 
d
i
r
e
c
t
o
r
i
e
s
 
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
 
e
x
t
r
a
c
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


 
 
 
 
 
 
 
 
l
i
s
t
:
 
A
 
l
i
s
t
 
o
f
 
d
i
c
t
i
o
n
a
r
i
e
s
 
e
x
t
r
a
c
t
e
d
 
a
n
d
 
p
a
r
s
e
d
 
f
r
o
m
 
t
h
e
 
f
i
l
e
s
 
i
n
 
t
h
e
 
d
i
r
e
c
t
o
r
i
e
s
.


 
 
 
 
"
"
"


 
 
 
 
p
a
r
s
e
_
d
i
c
t
s
 
=
 
[
]


 
 
 
 
f
o
r
 
d
i
r
_
p
a
t
h
 
i
n
 
d
i
r
_
p
a
t
h
s
:


 
 
 
 
 
 
 
 
p
a
r
s
e
import unittest
from unittest.mock import mock_open, patch


class TestExtractParseDicts(unittest.TestCase):
    def test_extract_single_valid_dictionary(self):
        mock_content = '{"name": "John", "age": 30}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [{"name": "John", "age": 30}])

    def test_extract_multiple_dictionaries(self):
        mock_content = '{"name": "John", "age": 30}\n{"city": "New York", "country": "USA"}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [{"name": "John", "age": 30}, {"city": "New York", "country": "USA"}])

    def test_invalid_dictionary_format(self):
        mock_content = '{"name": "John", "age": "thirty"}'
        with patch('builtins.open', mock_open(read_data=mock_content)):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [{'name': 'John', 'age': 'thirty'}])

    def test_empty_file(self):
        with patch('builtins.open', mock_open(read_data='')):
            result = extract_parse_dicts('dummy_path')
            self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()