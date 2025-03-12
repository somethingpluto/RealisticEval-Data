i
m
p
o
r
t
 
r
e






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
l
o
g
_
l
e
v
e
l
s
(
l
o
g
_
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
,
 
o
u
t
p
u
t
_
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
:


 
 
 
 
"
"
"


 
 
 
 
O
b
t
a
i
n
 
l
o
g
s
 
o
f
 
[
W
A
R
N
I
N
G
]
,
 
[
E
R
R
O
R
]
,
 
[
C
R
I
T
I
C
A
L
]
,
 
a
n
d
 
[
A
L
E
R
T
]
 
l
e
v
e
l
s
 
f
r
o
m
 
t
h
e
 
l
o
g
 
f
i
l
e


 
 
 
 
l
o
g
 
c
o
n
t
e
n
t
 
s
u
c
h
 
a
s
:


 
 
 
 
 
 
 
 
[
I
N
F
O
]
 
I
n
f
o
r
m
a
t
i
o
n
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
[
W
A
R
N
I
N
G
]
 
W
a
r
n
i
n
g
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
[
D
E
B
U
G
]
 
D
e
b
u
g
 
m
e
s
s
a
g
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
o
g
_
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
 
l
o
g
 
f
i
l
e
 
p
a
t
h


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
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
 
o
u
t
p
u
t
 
l
o
g
 
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


 
 
 
 
l
o
g
_
l
e
v
e
l
s
 
=
 
[
'
W
A
R
N
I
N
G
'
,
 
'
E
R
R
O
R
'
,
 
'
C
R
I
T
I
C
A
L
'
,
 
'
A
L
E
R
T
'
]


 
 
 
 
w
i
t
h
 
o
p
e
n
(
l
o
g
_
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


 
 
 
 
 
 
 
 
l
o
g
_
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


 
 
 
 
w
i
t
h
 
o
p
e
n
(
o
u
t
p
u
t
_
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
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
f
o
r
 
l
o
g
_
l
i
n
e
 
i
n
 
l
o
g
_
l
i
n
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
l
o
g
_
l
e
v
e
l
 
i
n
 
l
o
g
_
l
e
v
e
l
s
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
l
o
g
_
l
e
v
e
l
 
i
n
 
l
o
g
_
l
i
n
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
l
o
g
_
l
i
n
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k






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
l
o
g
_
l
e
v
e
l
s
_
w
i
t
h
_
r
e
g
e
x
(
l
o
g
_
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
,
 
o
u
t
p
u
t
_
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
:


 
 
 
 
"
"
"


 
 
 
 
O
b
t
a
i
n
 
l
o
g
s
 
o
f
 
[
W
A
R
N
I
N
G
]
,
 
[
E
R
R
O
R
]
,
 
[
C
R
I
T
I
C
A
L
]
,
 
a
n
d
 
[
A
L
E
R
T
]
 
l
e
v
e
l
s
 
f
r
o
m
 
t
h
e
 
l
o
g
 
f
i
l
e


 
 
 
 
l
o
g
 
c
o
n
t
e
n
t
 
s
u
c
h
 
a
s
:


 
 
 
 
 
 
 
 
[
I
N
F
O
]
 
I
n
f
o
r
m
a
t
i
o
n
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
[
W
A
R
N
I
N
G
]
 
W
a
r
n
i
n
g
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
[
D
E
B
U
G
]
 
D
e
b
u
g
 
m
e
s
s
a
g
e




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
l
o
g
_
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
 
l
o
g
 
f
i
l
e
 
p
a
t
h


 
 
 
 
 
 
 
 
o
u
t
p
u
t
_
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
 
o
u
t
p
u
t
 
l
o
g
 
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


 
 
 
 
l
o
g
_
l
e
v
e
l
s
 
=
 
[
'
W
A
R
N
I
N
G
'
,
 
'
E
R
R
O
R
'
,
 
'
C
R
I
T
I
C
A
L
'
,
 
'
A
L
E
R
T
'
]


 
 
 
 
w
i
t
h
 
o
p
e
n
(
l
o
g
_
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


 
 
 
 
 
 
 
 
l
o
g
_
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


 
 
 
 
w
i
t
h
 
o
p
e
n
(
o
u
t
p
u
t
_
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
w
'
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
f
o
r
 
l
o
g
_
l
i
n
e
 
i
n
 
l
o
g
_
l
i
n
e
s
:


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
l
o
g
_
l
e
v
e
l
 
i
n
 
l
o
g
_
l
e
v
e
l
s
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
r
e
.
s
e
a
r
c
h
(
l
o
g
_
l
e
v
e
l
,
 
l
o
g
_
l
i
n
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
l
o
g
_
l
i
n
e
)


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
b
r
e
a
k






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
l
o
g
_
l
e
v
e
l
s
_
w
i
t
h
_
r
e
g
e
x
_
a
n
d
_
g
r
o
u
p
(
l
o
g
_
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
,
 
o
u
t
p
u
t
_
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
:


 
 
 
 
"
"
"


 
 
 
 
O
b
t
a
i
n
import unittest
import tempfile
import os


# Assuming the extract_log_levels function is defined here or imported

class TestLogExtraction(unittest.TestCase):
    def create_temp_log_file(self, content):
        # Create a temporary log file
        temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        temp_file.write(content)
        temp_file.close()
        return temp_file.name

    def read_output_file(self, file_path):
        # Read content from a file
        with open(file_path, 'r') as file:
            return file.read()

    def test_warning_level(self):
        logs = """[INFO] Information message
[WARNING] Warning message
[DEBUG] Debug message"""
        expected_output = "[WARNING] Warning message\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_error_level(self):
        logs = """[ERROR] Error occurred
[INFO] Just an info"""
        expected_output = "[ERROR] Error occurred\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_critical_and_alert_levels(self):
        logs = """[ALERT] Security breach
[CRITICAL] System failure
[NOTICE] Something to notice"""
        expected_output = "[ALERT] Security breach\n[CRITICAL] System failure\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_no_relevant_logs(self):
        logs = "[INFO] No issues here\n[DEBUG] All systems go"
        expected_output = ""

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

    def test_mixed_logs(self):
        logs = """[WARNING] Low disk space
[INFO] Update completed
[ERROR] Failed to load module
[CRITICAL] Memory leak detected
[DEBUG] This is a debug message"""
        expected_output = "[WARNING] Low disk space\n[ERROR] Failed to load module\n[CRITICAL] Memory leak detected\n"

        log_file_path = self.create_temp_log_file(logs)
        output_file_path = tempfile.NamedTemporaryFile(delete=False).name

        extract_log_levels(log_file_path, output_file_path)

        result = self.read_output_file(output_file_path)
        self.assertEqual(result, expected_output)

        os.unlink(log_file_path)
        os.unlink(output_file_path)

if __name__ == '__main__':
    unittest.main()