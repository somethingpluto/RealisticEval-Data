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
e
n
t
r
i
e
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
)
:


 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
 
l
o
g
 
e
n
t
r
i
e
s
 
f
r
o
m
 
a
 
l
o
g
 
f
i
l
e
 
f
o
r
 
W
A
R
N
I
N
G
,
 
E
R
R
O
R
,
 
C
R
I
T
I
C
A
L
,
 
a
n
d
 
A
L
E
R
T
 
l
e
v
e
l
s


 
 
 
 
a
n
d
 
s
a
v
e
 
e
a
c
h
 
t
y
p
e
 
o
f
 
l
o
g
 
e
n
t
r
y
 
t
o
 
a
 
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
.




 
 
 
 
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
 
P
a
t
h
 
t
o
 
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






 
 
 
 
"
"
"


 
 
 
 
E
x
t
r
a
c
t
 
l
o
g
 
e
n
t
r
i
e
s
 
f
r
o
m
 
a
 
l
o
g
 
f
i
l
e
 
f
o
r
 
W
A
R
N
I
N
G
,
 
E
R
R
O
R
,
 
C
R
I
T
I
C
A
L
,
 
a
n
d
 
A
L
E
R
T
 
l
e
v
e
l
s


 
 
 
 
a
n
d
 
s
a
v
e
 
e
a
c
h
 
t
y
p
e
 
o
f
 
l
o
g
 
e
n
t
r
y
 
t
o
 
a
 
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
.




 
 
 
 
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
 
l
o
g
 
f
i
l
e
.


 
 
 
 
"
"
"




 
 
 
 
#
 
O
p
e
n
 
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
 
l
o
g
_
f
i
l
e
:




 
 
 
 
 
 
 
 
#
 
R
e
a
d
 
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
i
n
e
 
b
y
 
l
i
n
e


 
 
 
 
 
 
 
 
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
o
g
_
f
i
l
e
:




 
 
 
 
 
 
 
 
 
 
 
 
#
 
E
x
t
r
a
c
t
 
t
h
e
 
l
o
g
 
l
e
v
e
l


 
 
 
 
 
 
 
 
 
 
 
 
l
o
g
_
l
e
v
e
l
 
=
 
l
i
n
e
.
s
p
l
i
t
(
'
 
'
)
[
0
]




 
 
 
 
 
 
 
 
 
 
 
 
#
 
E
x
t
r
a
c
t
 
t
h
e
 
l
o
g
 
m
e
s
s
a
g
e


 
 
 
 
 
 
 
 
 
 
 
 
l
o
g
_
m
e
s
s
a
g
e
 
=
 
'
 
'
.
j
o
i
n
(
l
i
n
e
.
s
p
l
i
t
(
'
 
'
)
[
1
:
]
)




 
 
 
 
 
 
 
 
 
 
 
 
#
 
S
a
v
e
 
t
h
e
 
l
o
g
 
e
n
t
r
y
 
t
o
 
t
h
e
 
a
p
p
r
o
p
r
i
a
t
e
 
f
i
l
e


 
 
 
 
 
 
 
 
 
 
 
 
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
 
=
=
 
'
W
A
R
N
I
N
G
'
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
'
l
o
g
_
f
i
l
e
s
/
w
a
r
n
i
n
g
_
l
o
g
_
e
n
t
r
i
e
s
.
t
x
t
'
,
 
'
a
'
)
 
a
s
 
w
a
r
n
i
n
g
_
l
o
g
_
f
i
l
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
a
r
n
i
n
g
_
l
o
g
_
f
i
l
e
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
m
e
s
s
a
g
e
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
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
 
=
=
 
'
E
R
R
O
R
'
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
'
l
o
g
_
f
i
l
e
s
/
e
r
r
o
r
_
l
o
g
_
e
n
t
r
i
e
s
.
t
x
t
'
,
 
'
a
'
)
 
a
s
 
e
r
r
o
r
_
l
o
g
_
f
i
l
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
r
r
o
r
_
l
o
g
_
f
i
l
e
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
m
e
s
s
a
g
e
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
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
 
=
=
 
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
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
'
l
o
g
_
f
i
l
e
s
/
c
r
i
t
i
c
a
l
_
l
o
g
_
e
n
t
r
i
e
s
.
t
x
t
'
,
 
'
a
'
)
 
a
s
 
c
r
i
t
i
c
a
l
_
l
o
g
_
f
i
l
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
r
i
t
i
c
a
l
_
l
o
g
_
f
i
l
e
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
m
e
s
s
a
g
e
)


 
 
 
 
 
 
 
 
 
 
 
 
e
l
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
 
=
=
 
'
A
L
E
R
T
'
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
w
i
t
h
 
o
p
e
n
(
'
l
o
g
_
f
i
l
e
s
/
a
l
e
r
t
_
l
o
g
_
e
n
t
r
i
e
s
.
t
x
t
'
,
 
'
a
'
)
 
a
s
 
a
l
e
r
t
_
l
o
g
_
f
i
l
e
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
l
e
r
t
_
l
o
g
_
f
i
l
e
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
m
e
s
s
a
g
e
)






#
 
T
e
s
t
 
t
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
e
n
t
r
i
e
s
(
'
l
o
g
_
f
i
l
e
s
/
e
x
a
m
p
l
e
_
l
o
g
_
f
i
l
e
.
l
o
g
'
)


import unittest
import os


class TestExtractLogEntries(unittest.TestCase):

    def setUp(self):
        """Setup a temporary log file with sample question for testing."""
        self.log_file_path = 'test_log.log'
        self.log_contents = [
            "INFO: This is an informational message.\n",
            "WARNING: This is a warning message.\n",
            "ERROR: This is an error message.\n",
            "CRITICAL: This is a critical message.\n",
            "ALERT: This is an alert message.\n"
        ]
        with open(self.log_file_path, 'w') as log_file:
            log_file.writelines(self.log_contents)



    def test_no_logs_of_certain_levels(self):
        """Test the situation where there are no log entries for one or more levels."""
        with open(self.log_file_path, 'w') as log_file:
            log_file.write("INFO: This is another informational message.\n")
        extract_log_entries(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                self.assertEqual('', file.read())

    def test_file_not_found(self):
        """Test behavior when the log file does not exist."""
        with self.assertRaises(FileNotFoundError):
            extract_log_entries("nonexistent.log")

    def test_empty_log_file(self):
        """Test behavior with an empty log file."""
        with open(self.log_file_path, 'w') as log_file:
            log_file.write("")
        extract_log_entries(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                self.assertEqual('', file.read())

    def test_mixed_content_log_file(self):
        """Test extracting logs from a file with mixed content."""
        with open(self.log_file_path, 'w') as log_file:
            log_file.writelines([
                "INFO: Some info.\n",
                "WARNING: Watch out!\n",
                "DEBUG: Debugging.\n",
                "ERROR: Oops!\n",
                "CRITICAL: Failed badly.\n",
                "ALERT: High alert!\n",
                "INFO: More info.\n"
            ])
        extract_log_entries(self.log_file_path)
        for level in ['WARNING', 'ERROR', 'CRITICAL', 'ALERT']:
            with open(f"{level.lower()}_logs.txt", 'r') as file:
                content = file.read().strip()
                self.assertIn(level, content)

if __name__ == '__main__':
    unittest.main()