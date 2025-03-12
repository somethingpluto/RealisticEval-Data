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
d
a
t
e
_
f
r
o
m
_
f
i
l
e
n
a
m
e
(
f
i
l
e
_
n
a
m
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
d
a
t
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
Y
Y
Y
Y
-
M
M
-
D
D
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
f
i
l
e
 
n
a
m
e
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
n
a
m
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
 
n
a
m
e
 
o
f
 
t
h
e
 
f
i
l
e
 
w
h
i
c
h
 
m
a
y
 
c
o
n
t
a
i
n
 
a
 
d
a
t
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
 
o
r
 
N
o
n
e
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
d
a
t
e
 
s
t
r
i
n
g
 
i
n
 
Y
Y
Y
Y
-
M
M
-
D
D
 
f
o
r
m
a
t
 
i
f
 
f
o
u
n
d
,
 
e
l
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
d
a
t
e
_
p
a
t
t
e
r
n
 
=
 
r
e
.
c
o
m
p
i
l
e
(
r
'
\
d
{
4
}
-
\
d
{
2
}
-
\
d
{
2
}
'
)


 
 
 
 
m
a
t
c
h
 
=
 
d
a
t
e
_
p
a
t
t
e
r
n
.
s
e
a
r
c
h
(
f
i
l
e
_
n
a
m
e
)


 
 
 
 
i
f
 
m
a
t
c
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
t
c
h
.
g
r
o
u
p
(
0
)


 
 
 
 
r
e
t
u
r
n
 
N
o
n
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
d
a
t
e
_
f
r
o
m
_
f
i
l
e
_
c
o
n
t
e
n
t
(
f
i
l
e
_
c
o
n
t
e
n
t
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
s
 
t
h
e
 
d
a
t
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
Y
Y
Y
Y
-
M
M
-
D
D
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
f
i
l
e
 
c
o
n
t
e
n
t
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
c
o
n
t
e
n
t
 
(
s
t
r
)
:
 
T
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
f
i
l
e
 
w
h
i
c
h
 
m
a
y
 
c
o
n
t
a
i
n
 
a
 
d
a
t
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
 
o
r
 
N
o
n
e
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
d
a
t
e
 
s
t
r
i
n
g
 
i
n
 
Y
Y
Y
Y
-
M
M
-
D
D
 
f
o
r
m
a
t
 
i
f
 
f
o
u
n
d
,
 
e
l
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
d
a
t
e
_
p
a
t
t
e
r
n
 
=
 
r
e
.
c
o
m
p
i
l
e
(
r
'
\
d
{
4
}
-
\
d
{
2
}
-
\
d
{
2
}
'
)


 
 
 
 
m
a
t
c
h
 
=
 
d
a
t
e
_
p
a
t
t
e
r
n
.
s
e
a
r
c
h
(
f
i
l
e
_
c
o
n
t
e
n
t
)


 
 
 
 
i
f
 
m
a
t
c
h
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
m
a
t
c
h
.
g
r
o
u
p
(
0
)


 
 
 
 
r
e
t
u
r
n
 
N
o
n
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
d
a
t
e
_
f
r
o
m
_
f
i
l
e
_
c
o
n
t
e
n
t
_
w
i
t
h
_
d
a
t
e
_
i
n
_
f
i
l
e
n
a
m
e
(
f
i
l
e
_
c
o
n
t
e
n
t
:
 
s
t
r
,
 
f
i
l
e
_
n
a
m
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


 
 
 
 
E
x
t
r
a
c
t
s
 
t
h
e
 
d
a
t
e
 
i
n
 
t
h
e
 
f
o
r
m
a
t
 
Y
Y
Y
Y
-
M
M
-
D
D
 
f
r
o
m
 
t
h
e
 
g
i
v
e
n
 
f
i
l
e
 
c
o
n
t
e
n
t
 
a
n
d
 
f
i
l
e
 
n
a
m
e
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
c
o
n
t
e
n
t
 
(
s
t
r
)
:
 
T
h
e
 
c
o
n
t
e
n
t
 
o
f
 
t
h
e
 
f
i
l
e
 
w
h
i
c
h
 
m
a
y
 
c
o
n
t
a
i
n
 
a
 
d
a
t
e
.


 
 
 
 
 
 
 
 
f
i
l
e
_
n
a
m
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
 
n
a
m
e
 
o
f
 
t
h
e
 
f
i
l
e
 
w
h
i
c
h
 
m
a
y
 
c
o
n
t
a
i
n
 
a
 
d
a
t
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
 
o
r
 
N
o
n
e
:
 
T
h
e
 
e
x
t
r
a
c
t
e
d
 
d
a
t
e
 
s
t
r
i
n
g
 
i
n
 
Y
Y
Y
Y
-
M
M
-
D
D
 
f
o
r
m
a
t
 
i
f
 
f
o
u
n
d
,
 
e
l
s
e
 
N
o
n
e
.


 
 
 
 
"
"
"


 
 
 
 
d
a
t
e
_
p
a
t
t
e
r
n
 
=
 
r
e
.
c
o
m
p
i
l
e
(
r
'
\
d
{
4
}
-
\
d
{
2
}
-
\
d
{
2
}
'
)


 
 
 
 
m
a
t
c
h
 
=
 
d
a
t
e
_
p
a
t
t
e
r
n
.
s
e
a
r
c
h
(
f
i
l
e
_
c
o
n
t
e
n
t
)


 
 
 
 
i
f
 
m
a
t
c
h
:
import unittest


class TestExtractDateFromFilename(unittest.TestCase):

    def test_date_extraction_success(self):
        """Test case where the date is successfully extracted."""
        file_name = "report-2023-09-28.txt"
        expected_date = "2023-09-28"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

    def test_no_date_in_filename(self):
        """Test case where no date is present in the filename."""
        file_name = "report.txt"
        self.assertIsNone(extract_date_from_filename(file_name))

    def test_multiple_dates_in_filename(self):
        """Test case where multiple dates are present, should return the first one."""
        file_name = "report-2023-09-28-backup-2023-10-01.txt"
        expected_date = "2023-09-28"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

    def test_date_at_start_of_filename(self):
        """Test case where the date is at the start of the filename."""
        file_name = "2023-09-28-report.txt"
        expected_date = "2023-09-28"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

    def test_incorrect_date_format(self):
        """Test case where the date format is incorrect."""
        file_name = "report-2023-99-99.txt"  # Invalid date
        expected_date = "2023-99-99"
        self.assertEqual(extract_date_from_filename(file_name), expected_date)

if __name__ == '__main__':
    unittest.main()