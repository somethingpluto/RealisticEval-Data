i
m
p
o
r
t
 
p
a
n
d
a
s
 
a
s
 
p
d






d
e
f
 
t
s
v
_
t
o
_
j
s
o
n
l
(
t
s
v
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
 
j
s
o
n
l
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
 
t
s
v
 
f
i
l
e
 
t
o
 
j
s
o
n
l
 
f
i
l
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
t
s
v
_
f
i
l
e
:
 
t
s
f
 
f
i
l
e
 
p
a
t
h


 
 
 
 
 
 
 
 
j
s
o
n
l
_
f
i
l
e
:
 
j
s
o
n
l
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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


 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
c
s
v
(
t
s
v
_
f
i
l
e
,
 
s
e
p
=
'
\
t
'
)


 
 
 
 
d
f
.
t
o
_
j
s
o
n
(
j
s
o
n
l
_
f
i
l
e
,
 
o
r
i
e
n
t
=
'
r
e
c
o
r
d
s
'
,
 
l
i
n
e
s
=
T
r
u
e
)






d
e
f
 
j
s
o
n
l
_
t
o
_
t
s
v
(
j
s
o
n
l
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
 
t
s
v
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
 
j
s
o
n
l
 
f
i
l
e
 
t
o
 
t
s
v
 
f
i
l
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
l
_
f
i
l
e
:
 
j
s
o
n
l
 
f
i
l
e
 
p
a
t
h


 
 
 
 
 
 
 
 
t
s
v
_
f
i
l
e
:
 
t
s
v
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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


 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
j
s
o
n
(
j
s
o
n
l
_
f
i
l
e
,
 
l
i
n
e
s
=
T
r
u
e
)


 
 
 
 
d
f
.
t
o
_
c
s
v
(
t
s
v
_
f
i
l
e
,
 
s
e
p
=
'
\
t
'
,
 
i
n
d
e
x
=
F
a
l
s
e
)






d
e
f
 
j
s
o
n
l
_
t
o
_
t
s
v
_
w
i
t
h
_
h
e
a
d
e
r
(
j
s
o
n
l
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
 
t
s
v
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
 
j
s
o
n
l
 
f
i
l
e
 
t
o
 
t
s
v
 
f
i
l
e
 
w
i
t
h
 
h
e
a
d
e
r




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
l
_
f
i
l
e
:
 
j
s
o
n
l
 
f
i
l
e
 
p
a
t
h


 
 
 
 
 
 
 
 
t
s
v
_
f
i
l
e
:
 
t
s
v
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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


 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
j
s
o
n
(
j
s
o
n
l
_
f
i
l
e
,
 
l
i
n
e
s
=
T
r
u
e
)


 
 
 
 
d
f
.
t
o
_
c
s
v
(
t
s
v
_
f
i
l
e
,
 
s
e
p
=
'
\
t
'
,
 
i
n
d
e
x
=
F
a
l
s
e
,
 
h
e
a
d
e
r
=
T
r
u
e
)






d
e
f
 
j
s
o
n
l
_
t
o
_
t
s
v
_
w
i
t
h
_
h
e
a
d
e
r
_
a
n
d
_
i
n
d
e
x
(
j
s
o
n
l
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
 
t
s
v
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
 
j
s
o
n
l
 
f
i
l
e
 
t
o
 
t
s
v
 
f
i
l
e
 
w
i
t
h
 
h
e
a
d
e
r
 
a
n
d
 
i
n
d
e
x




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
j
s
o
n
l
_
f
i
l
e
:
 
j
s
o
n
l
 
f
i
l
e
 
p
a
t
h


 
 
 
 
 
 
 
 
t
s
v
_
f
i
l
e
:
 
t
s
v
 
f
i
l
e
 
p
a
t
h




 
 
 
 
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


 
 
 
 
d
f
 
=
 
p
d
.
r
e
a
d
_
j
s
o
n
(
j
s
o
n
l
_
f
i
l
e
,
 
l
i
n
e
s
=
T
r
u
e
)


 
 
 
 
d
f
.
t
o
_
c
s
v
(
t
s
v
_
f
i
l
e
,
 
s
e
p
=
'
\
t
'
,
 
i
n
d
e
x
=
T
r
u
e
,
 
h
e
a
d
e
r
=
T
r
u
e
)






d
e
f
 
j
s
o
n
l
_
t
o
_
t
s
v
_
w
i
t
h
_
h
e
a
d
e
r
_
a
n
d
_
i
n
d
e
x
_
a
n
d
_
c
o
l
u
m
n
s
import os
import tempfile
import unittest


class TestTSVtoJSONL(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Clean up the temporary directory
        self.test_dir.cleanup()

    def test_standard_tsv(self):
        tsv_content = "Name\tAge\tCountry\nAlice\t30\tUSA\nBob\t25\tCanada\n"
        tsv_file = os.path.join(self.test_dir.name, 'test_standard.tsv')
        jsonl_file = os.path.join(self.test_dir.name, 'test_standard.jsonl')

        with open(tsv_file, 'w', encoding='utf-8') as f:
            f.write(tsv_content)

        tsv_to_jsonl(tsv_file, jsonl_file)

        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        expected_lines = [
            '{"Name":"Alice","Age":30,"Country":"USA"}\n',
            '{"Name":"Bob","Age":25,"Country":"Canada"}\n'
        ]
        self.assertEqual(lines, expected_lines)


    def test_single_row_tsv(self):
        tsv_content = "Name\tAge\tCountry\nAlice\t30\tUSA\n"
        tsv_file = os.path.join(self.test_dir.name, 'test_single_row.tsv')
        jsonl_file = os.path.join(self.test_dir.name, 'test_single_row.jsonl')

        with open(tsv_file, 'w', encoding='utf-8') as f:
            f.write(tsv_content)

        tsv_to_jsonl(tsv_file, jsonl_file)

        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        expected_lines = [
            '{"Name":"Alice","Age":30,"Country":"USA"}\n'
        ]
        self.assertEqual(lines, expected_lines)

    def test_numeric_and_boolean_values(self):
        tsv_content = "Name\tAge\tIs_Student\nAlice\t30\tTrue\nBob\t25\tFalse\n"
        tsv_file = os.path.join(self.test_dir.name, 'test_numeric_boolean.tsv')
        jsonl_file = os.path.join(self.test_dir.name, 'test_numeric_boolean.jsonl')

        with open(tsv_file, 'w', encoding='utf-8') as f:
            f.write(tsv_content)

        tsv_to_jsonl(tsv_file, jsonl_file)

        with open(jsonl_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        expected_lines = [
            '{"Name":"Alice","Age":30,"Is_Student":true}\n',
            '{"Name":"Bob","Age":25,"Is_Student":false}\n'
        ]
        self.assertEqual(lines, expected_lines)

if __name__ == '__main__':
    unittest.main()