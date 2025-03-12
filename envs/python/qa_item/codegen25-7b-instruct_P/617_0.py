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
 
A
n
y






d
e
f
 
p
a
r
s
e
_
j
s
o
n
_
f
i
l
e
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
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
J
S
O
N
 
f
i
l
e
 
a
n
d
 
s
t
o
r
e
s
 
i
t
s
 
c
o
n
t
e
n
t
s
 
i
n
 
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
 
J
S
O
N
 
f
i
l
e
 
t
o
 
b
e
 
p
a
r
s
e
d
.
 
T
h
e
 
f
i
l
e
 
m
u
s
t
 
e
x
i
s
t
 
a
n
d
 
c
o
n
t
a
i
n
 
v
a
l
i
d
 
J
S
O
N
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
p
a
t
h
 
s
h
o
u
l
d
 
b
e
 
a
 
f
u
l
l
y
 
q
u
a
l
i
f
i
e
d
 
p
a
t
h
 
o
r
 
r
e
l
a
t
i
v
e
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
w
o
r
k
i
n
g
 
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
[
s
t
r
,
 
A
n
y
]
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
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
 
J
S
O
N
 
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
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
j
s
o
n
.
l
o
a
d
(
f
)






d
e
f
 
p
a
r
s
e
_
j
s
o
n
_
s
t
r
i
n
g
(
j
s
o
n
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
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
J
S
O
N
 
s
t
r
i
n
g
 
a
n
d
 
s
t
o
r
e
s
 
i
t
s
 
c
o
n
t
e
n
t
s
 
i
n
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
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
 
J
S
O
N
 
s
t
r
i
n
g
 
t
o
 
b
e
 
p
a
r
s
e
d
.
 
T
h
e
 
s
t
r
i
n
g
 
m
u
s
t
 
c
o
n
t
a
i
n
 
v
a
l
i
d
 
J
S
O
N
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
[
s
t
r
,
 
A
n
y
]
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
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
 
J
S
O
N
 
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


 
 
 
 
r
e
t
u
r
n
 
j
s
o
n
.
l
o
a
d
s
(
j
s
o
n
_
s
t
r
i
n
g
)






d
e
f
 
p
a
r
s
e
_
y
a
m
l
_
f
i
l
e
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
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
Y
A
M
L
 
f
i
l
e
 
a
n
d
 
s
t
o
r
e
s
 
i
t
s
 
c
o
n
t
e
n
t
s
 
i
n
 
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
 
Y
A
M
L
 
f
i
l
e
 
t
o
 
b
e
 
p
a
r
s
e
d
.
 
T
h
e
 
f
i
l
e
 
m
u
s
t
 
e
x
i
s
t
 
a
n
d
 
c
o
n
t
a
i
n
 
v
a
l
i
d
 
Y
A
M
L
.


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
T
h
e
 
p
a
t
h
 
s
h
o
u
l
d
 
b
e
 
a
 
f
u
l
l
y
 
q
u
a
l
i
f
i
e
d
 
p
a
t
h
 
o
r
 
r
e
l
a
t
i
v
e
 
t
o
 
t
h
e
 
c
u
r
r
e
n
t
 
w
o
r
k
i
n
g
 
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
[
s
t
r
,
 
A
n
y
]
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
 
k
e
y
-
v
a
l
u
e
 
p
a
i
r
s
 
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
 
Y
A
M
L
 
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
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
y
a
m
l
.
s
a
f
e
_
l
o
a
d
(
f
)






d
e
f
 
p
a
r
s
e
_
y
a
m
l
_
s
t
r
i
n
g
(
y
a
m
l
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
 
D
i
c
t
[
s
t
r
,
 
A
n
y
]
:


 
 
 
 
"
"
"


 
 
 
 
P
a
r
s
e
s
 
a
 
Y
A
M
L
 
s
t
r
i
n
g
 
a
n
d
 
s
t
o
r
e
s
 
i
t
s
 
c
o
n
t
e
n
t
s
 
i
n
 
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




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
y
a
m
l
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
 
Y
A
M
L
 
s
t
r
i
n
g
 
t
o
 
b
e
 
p
a
r
s
e
d
.
 
T
h
e
 
s
t
r
i
n
g
 
m
u
s
t
 
c
o
n
t
a
i
n
 
v
a
l
i
d
 
Y
A
M
L
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
[
s
t
r
,
 
A
n
y
]
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
import json
import os
import unittest


class Tester(unittest.TestCase):

    def test_valid_json(self):
        json_content = '{"name": "John", "age": 30}'
        path = 'temp_valid.json'

        with open(path, 'w') as temp_file:
            temp_file.write(json_content)

        result = parse_json_file(path)
        self.assertEqual("John", result.get("name"))
        self.assertEqual(30, result.get("age"))

        os.remove(path)  # Clean up the temporary file

    def test_empty_json(self):
        json_content = '{}'
        path = 'temp_empty.json'

        with open(path, 'w') as temp_file:
            temp_file.write(json_content)

        result = parse_json_file(path)
        self.assertTrue(len(result) == 0)

        os.remove(path)  # Clean up the temporary file

    def test_null_input(self):
        with self.assertRaises(Exception):
            parse_json_file(None)

    def test_non_json_file(self):
        not_json_content = "Hello, World!"
        path = 'temp_not_json.txt'

        with open(path, 'w') as temp_file:
            temp_file.write(not_json_content)

        with self.assertRaises(json.JSONDecodeError):
            parse_json_file(path)

        os.remove(path)  # Clean up the temporary file

    def test_json_with_array(self):
        json_content = '{"names": ["John", "Doe"]}'
        path = 'temp_array.json'

        with open(path, 'w') as temp_file:
            temp_file.write(json_content)

        result = parse_json_file(path)
        self.assertIsNotNone(result.get("names"))

        os.remove(path)  # Clean up the temporary file
if __name__ == '__main__':
    unittest.main()