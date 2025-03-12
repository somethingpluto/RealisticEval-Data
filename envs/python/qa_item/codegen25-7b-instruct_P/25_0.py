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
l
a
s
s
i
f
y
_
j
s
o
n
_
o
b
j
e
c
t
s
_
b
y
_
p
i
d
(
s
o
u
r
c
e
_
f
i
l
e
:
 
s
t
r
,
 
p
i
d
_
l
i
s
t
:
 
L
i
s
t
[
i
n
t
]
,
 
m
a
t
c
h
_
f
i
l
e
:
 
s
t
r
,
 
m
i
s
m
a
t
c
h
_
f
i
l
e
:
 
s
t
r
)
 
-
>
 
N
o
n
e
:


 
 
 
 
"
"
"


 
 
 
 
r
e
a
d
 
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
 
q
u
e
s
t
i
o
n
 
b
a
s
e
d
 
o
n
 
w
h
e
t
h
e
r
 
t
h
e
 
p
i
d
 
f
i
e
l
d
 
i
n
 
t
h
e
 
o
b
j
e
c
t
 
i
s
 
i
n
c
l
u
d
e
d
 
i
n
 
a
 
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
i
d
_
l
i
s
t
.
 
T
h
e
s
e
 
o
b
j
e
c
t
s
 
a
r
e
 
t
h
e
n
 
c
l
a
s
s
i
f
i
e
d
 
i
n
t
o
 
t
w
o
 
c
a
t
e
g
o
r
i
e
s
 
b
a
s
e
d
 
o
n
 
m
a
t
c
h
e
s
 
a
n
d
 
m
i
s
m
a
t
c
h
e
s
 
a
n
d
 
s
a
v
e
d
 
i
n
 
d
i
f
f
e
r
e
n
t
 
f
i
l
e
s




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
o
u
r
c
e
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
t
h
e
 
s
o
u
r
c
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


 
 
 
 
 
 
 
 
p
i
d
_
l
i
s
t
 
(
l
i
s
t
)
:
 
L
i
s
t
 
o
f
 
p
i
d
s
 
t
o
 
m
a
t
c
h
.


 
 
 
 
 
 
 
 
m
a
t
c
h
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
s
a
v
e
 
m
a
t
c
h
i
n
g
 
o
b
j
e
c
t
s
 
J
S
O
N
.


 
 
 
 
 
 
 
 
m
i
s
m
a
t
c
h
_
f
i
l
e
 
(
s
t
r
)
:
 
P
a
t
h
 
t
o
 
s
a
v
e
 
m
i
s
m
a
t
c
h
i
n
g
 
o
b
j
e
c
t
s
 
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
s
o
u
r
c
e
_
f
i
l
e
,
 
'
r
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
d
a
t
a
 
=
 
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




 
 
 
 
m
a
t
c
h
_
l
i
s
t
 
=
 
[
]


 
 
 
 
m
i
s
m
a
t
c
h
_
l
i
s
t
 
=
 
[
]


 
 
 
 
f
o
r
 
o
b
j
 
i
n
 
d
a
t
a
:


 
 
 
 
 
 
 
 
i
f
 
o
b
j
[
'
p
i
d
'
]
 
i
n
 
p
i
d
_
l
i
s
t
:


 
 
 
 
 
 
 
 
 
 
 
 
m
a
t
c
h
_
l
i
s
t
.
a
p
p
e
n
d
(
o
b
j
)


 
 
 
 
 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
 
 
 
 
m
i
s
m
a
t
c
h
_
l
i
s
t
.
a
p
p
e
n
d
(
o
b
j
)




 
 
 
 
w
i
t
h
 
o
p
e
n
(
m
a
t
c
h
_
f
i
l
e
,
 
'
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
j
s
o
n
.
d
u
m
p
(
m
a
t
c
h
_
l
i
s
t
,
 
f
)




 
 
 
 
w
i
t
h
 
o
p
e
n
(
m
i
s
m
a
t
c
h
_
f
i
l
e
,
 
'
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
j
s
o
n
.
d
u
m
p
(
m
i
s
m
a
t
c
h
_
l
i
s
t
,
 
f
)






d
e
f
 
m
a
i
n
(
)
:


 
 
 
 
p
a
r
s
e
r
 
=
 
a
r
g
p
a
r
s
e
.
A
r
g
u
m
e
n
t
P
a
r
s
e
r
(
d
e
s
c
r
i
p
t
i
o
n
=
'
C
l
a
s
s
i
f
y
 
J
S
O
N
 
o
b
j
e
c
t
s
 
b
y
 
P
I
D
.
'
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
'
s
o
u
r
c
e
_
f
i
l
e
'
,
 
t
y
p
e
=
s
t
r
,
 
h
e
l
p
=
'
P
a
t
h
 
t
o
 
t
h
e
 
s
o
u
r
c
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
'
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
'
p
i
d
_
l
i
s
t
'
,
 
t
y
p
e
=
i
n
t
,
 
n
a
r
g
s
=
'
+
'
,
 
h
e
l
p
=
'
L
i
s
t
 
o
f
 
p
i
d
s
 
t
o
 
m
a
t
c
h
.
'
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
'
m
a
t
c
h
_
f
i
l
e
'
,
 
t
y
p
e
=
s
t
r
,
 
h
e
l
p
=
'
P
a
t
h
 
t
o
 
s
a
v
e
 
m
a
t
c
h
i
n
g
 
o
b
j
e
c
t
s
 
J
S
O
N
.
'
)


 
 
 
 
p
a
r
s
e
r
.
a
d
d
_
a
r
g
u
m
e
n
t
(
'
m
i
s
m
a
t
c
h
_
f
i
l
e
'
,
 
t
y
p
e
=
s
t
r
,
 
h
e
l
p
=
'
P
a
t
h
 
t
o
 
s
a
v
e
 
m
i
s
m
a
t
c
h
i
n
g
 
o
b
j
e
c
t
s
 
J
S
O
N
.
'
)


 
 
 
 
a
r
g
s
 
=
 
p
a
r
s
e
r
.
p
a
r
s
e
_
a
r
g
s
(
)




 
 
 
 
c
l
a
s
s
i
f
y
_
j
s
o
n
_
o
b
j
e
c
t
s
_
b
y
_
p
i
d
(
a
r
g
s
.
s
o
u
r
c
e
_
f
i
l
e
,
 
a
r
g
s
.
p
i
d
_
l
i
s
t
,
 
a
r
g
s
.
m
a
t
c
h
_
f
i
l
e
,
 
a
r
g
s
.
m
i
s
m
a
t
c
h
_
f
i
l
e
)






i
f
 
_
_
n
a
m
e
_
_
 
=
=
 
'
_
_
m
a
i
n
_
_
'
:


 
 
 
 
m
a
i
n
(
)


import unittest
import json
import tempfile
import os

class TestClassifyJsonObjectsByPid(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.temp_dir = tempfile.mkdtemp()

        # Create temporary files for testing
        self.source_file = os.path.join(self.temp_dir, 'source.json')
        self.match_file = os.path.join(self.temp_dir, 'match.json')
        self.mismatch_file = os.path.join(self.temp_dir, 'mismatch.json')

        # Example question
        self.data = [
            {"name": "Alice", "pid": 1},
            {"name": "Bob", "pid": 2},
            {"name": "Charlie", "pid": 3}
        ]
        self.pid_list = [1, 3]

        # Write example question to source file
        with open(self.source_file, 'w') as f:
            json.dump(self.data, f)

    def test_all_match(self):
        # Test where all items match
        classify_json_objects_by_pid(self.source_file, [1, 2, 3], self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 3)
        self.assertEqual(len(mismatches), 0)

    def test_no_match(self):
        # Test where no items match
        classify_json_objects_by_pid(self.source_file, [4, 5], self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 0)
        self.assertEqual(len(mismatches), 3)

    def test_partial_match(self):
        # Test where some items match
        classify_json_objects_by_pid(self.source_file, self.pid_list, self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 2)
        self.assertEqual(len(mismatches), 1)

    def test_empty_pid_list(self):
        # Test with an empty PID list
        classify_json_objects_by_pid(self.source_file, [], self.match_file, self.mismatch_file)
        with open(self.match_file, 'r') as f:
            matches = json.load(f)
        with open(self.mismatch_file, 'r') as f:
            mismatches = json.load(f)
        self.assertEqual(len(matches), 0)
        self.assertEqual(len(mismatches), 3)

if __name__ == '__main__':
    unittest.main()