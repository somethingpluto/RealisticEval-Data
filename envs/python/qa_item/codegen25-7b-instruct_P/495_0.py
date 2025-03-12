i
m
p
o
r
t
 
r
e


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
 
f
i
l
t
e
r
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
c
o
n
t
e
x
t
(


 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
k
e
y
w
o
r
d
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
,


 
 
 
 
 
 
 
 
l
i
n
e
s
_
b
e
f
o
r
e
:
 
i
n
t
 
=
 
1
,


 
 
 
 
 
 
 
 
l
i
n
e
s
_
a
f
t
e
r
:
 
i
n
t
 
=
 
1


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


 
 
 
 
F
i
l
t
e
r
s
 
w
e
b
s
i
t
e
 
c
o
n
t
e
n
t
 
t
o
 
i
n
c
l
u
d
e
 
l
i
n
e
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
 
a
n
y
 
o
f
 
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
 
k
e
y
w
o
r
d
s
 
a
s
 
w
h
o
l
e
 
w
o
r
d
s
,


 
 
 
 
a
l
o
n
g
 
w
i
t
h
 
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
 
n
u
m
b
e
r
 
o
f
 
l
i
n
e
s
 
b
e
f
o
r
e
 
a
n
d
 
a
f
t
e
r
 
f
o
r
 
c
o
n
t
e
x
t
.
 
T
h
i
s
 
v
e
r
s
i
o
n
 
u
s
e
s
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
s


 
 
 
 
t
o
 
e
n
s
u
r
e
 
e
x
a
c
t
,
 
w
h
o
l
e
 
w
o
r
d
 
m
a
t
c
h
i
n
g
 
a
n
d
 
r
e
s
p
e
c
t
s
 
c
a
s
e
 
s
e
n
s
i
t
i
v
i
t
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
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
 
f
u
l
l
 
t
e
x
t
 
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
 
w
e
b
s
i
t
e
.


 
 
 
 
 
 
 
 
k
e
y
w
o
r
d
s
 
(
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
:
 
A
 
l
i
s
t
 
o
f
 
s
t
r
i
n
g
s
 
t
o
 
s
e
a
r
c
h
 
f
o
r
 
w
i
t
h
i
n
 
t
h
e
 
c
o
n
t
e
n
t
.


 
 
 
 
 
 
 
 
l
i
n
e
s
_
b
e
f
o
r
e
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
l
i
n
e
s
 
t
o
 
i
n
c
l
u
d
e
 
b
e
f
o
r
e
 
a
 
m
a
t
c
h
i
n
g
 
l
i
n
e
.


 
 
 
 
 
 
 
 
l
i
n
e
s
_
a
f
t
e
r
 
(
i
n
t
)
:
 
N
u
m
b
e
r
 
o
f
 
l
i
n
e
s
 
t
o
 
i
n
c
l
u
d
e
 
a
f
t
e
r
 
a
 
m
a
t
c
h
i
n
g
 
l
i
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
 
s
t
r
i
n
g
 
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
 
f
i
l
t
e
r
e
d
 
c
o
n
t
e
n
t
 
w
i
t
h
 
a
d
d
i
t
i
o
n
a
l
 
c
o
n
t
e
x
t
.


 
 
 
 
"
"
"


 
 
 
 
#
 
C
o
m
p
i
l
e
 
t
h
e
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
 
p
a
t
t
e
r
n
 
f
o
r
 
e
a
c
h
 
k
e
y
w
o
r
d


 
 
 
 
p
a
t
t
e
r
n
 
=
 
r
'
\
b
(
'
 
+
 
r
'
|
'
.
j
o
i
n
(
k
e
y
w
o
r
d
s
)
 
+
 
r
'
)
\
b
'


 
 
 
 
#
 
C
o
m
p
i
l
e
 
t
h
e
 
r
e
g
u
l
a
r
 
e
x
p
r
e
s
s
i
o
n
 
p
a
t
t
e
r
n
 
f
o
r
 
e
a
c
h
 
k
e
y
w
o
r
d


 
 
 
 
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
p
a
t
t
e
r
n
,
 
r
e
.
I
G
N
O
R
E
C
A
S
E
)


 
 
 
 
#
 
S
p
l
i
t
 
t
h
e
 
c
o
n
t
e
n
t
 
i
n
t
o
 
l
i
n
e
s


 
 
 
 
l
i
n
e
s
 
=
 
c
o
n
t
e
n
t
.
s
p
l
i
t
l
i
n
e
s
(
)


 
 
 
 
#
 
I
n
i
t
i
a
l
i
z
e
 
t
h
e
 
f
i
l
t
e
r
e
d
 
c
o
n
t
e
n
t


 
 
 
 
f
i
l
t
e
r
e
d
_
c
o
n
t
e
n
t
 
=
 
'
'


 
 
 
 
#
 
L
o
o
p
 
o
v
e
r
 
e
a
c
h
 
l
i
n
e
 
i
n
 
t
h
e
 
c
o
n
t
e
n
t


 
 
 
 
f
o
r
 
i
,
 
l
i
n
e
 
i
n
 
e
n
u
m
e
r
a
t
e
(
l
i
n
e
s
)
:


 
 
 
 
 
 
 
 
#
 
C
h
e
c
k
 
i
f
 
t
h
e
 
l
i
n
e
 
c
o
n
t
a
i
n
s
 
a
n
y
 
o
f
 
t
h
e
 
k
e
y
w
o
r
d
s


 
 
 
 
 
 
 
 
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
p
a
t
t
e
r
n
,
 
l
i
n
e
)
:


 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
t
h
e
 
l
i
n
e
 
t
o
 
t
h
e
 
f
i
l
t
e
r
e
d
 
c
o
n
t
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
e
d
_
c
o
n
t
e
n
t
 
+
=
 
l
i
n
e
 
+
 
'
\
n
'


 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
t
h
e
 
l
i
n
e
s
 
b
e
f
o
r
e
 
a
n
d
 
a
f
t
e
r
 
t
h
e
 
l
i
n
e
 
t
o
 
t
h
e
 
f
i
l
t
e
r
e
d
 
c
o
n
t
e
n
t


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
j
 
i
n
 
r
a
n
g
e
(
i
 
-
 
l
i
n
e
s
_
b
e
f
o
r
e
,
 
i
 
+
 
l
i
n
e
s
_
a
f
t
e
r
 
+
 
1
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
j
 
<
 
0
 
o
r
 
j
 
>
=
 
l
e
n
(
l
i
n
e
s
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
t
i
n
u
e


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
e
d
_
c
o
n
t
e
n
t
 
+
=
 
l
i
n
e
s
[
j
]
 
+
 
'
\
n
'


 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
a
 
n
e
w
l
i
n
e
 
t
o
 
s
e
p
a
r
a
t
e
 
t
h
e
 
c
o
n
t
e
x
t
 
f
r
o
m
 
t
h
e
 
n
e
x
t
 
k
e
y
w
o
r
d
 
m
a
t
c
h


 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
t
e
r
e
d
_
c
o
n
t
e
n
t
 
+
=
 
'
\
n
'


 
 
 
 
#
 
R
e
t
u
r
n
 
t
h
e
 
f
i
l
t
e
r
e
d
 
c
o
n
t
e
n
t


 
 
 
 
r
e
t
u
r
n
 
f
i
l
t
e
r
e
d
_
c
o
n
t
e
n
t






d
e
f
 
f
i
l
t
e
r
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
c
o
n
t
e
x
t
_
s
t
r
i
c
t
(


 
 
 
 
 
 
 
 
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


 
 
 
 
 
 
 
 
k
e
y
w
o
r
d
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
,


 
 
 
 
 
 
 
 
l
i
n
e
s
_
import unittest


class TestFilterContentWithContext(unittest.TestCase):

    def test_single_keyword_match(self):
        """Test a single keyword match with context lines."""
        content = """Line one.
        This line contains a keyword.
        Line three."""
        keywords = ["keyword"]
        expected_output = """Line one.
        This line contains a keyword.
        Line three."""
        result = filter_content_with_context(content, keywords, lines_before=1, lines_after=1)
        self.assertEqual(result.strip(), expected_output.strip(), "Failed to filter content for a single keyword.")


    def test_no_keyword_match(self):
        """Test when no keywords match."""
        content = """Line one.
        Line two.
        Line three."""
        keywords = ["missing"]
        expected_output = ""
        result = filter_content_with_context(content, keywords, lines_before=1, lines_after=1)
        self.assertEqual(result.strip(), expected_output, "Failed to return empty string for no matches.")


    def test_lines_before_and_after(self):
        """Test functionality with specified lines before and after."""
        content = """Line one.
        This line contains a keyword.
        Line three.
        Line four.
        Line five."""
        keywords = ["keyword"]
        expected_output = """Line one.
        This line contains a keyword.
        Line three."""
        result = filter_content_with_context(content, keywords, lines_before=1, lines_after=1)
        self.assertEqual(result.strip(), expected_output.strip(), "Failed to correctly include context lines.")

if __name__ == '__main__':
    unittest.main()