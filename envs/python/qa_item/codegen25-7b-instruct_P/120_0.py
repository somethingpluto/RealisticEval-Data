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
 
e
x
t
r
a
c
t
_
c
s
v
_
d
a
t
a
_
f
r
o
m
_
h
t
m
l
(
h
t
m
l
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
 
-
>
 
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
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
 
t
a
b
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
 
f
r
o
m
 
a
n
 
H
T
M
L
 
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
a
b
l
e
s
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
q
u
e
s
t
i
o
n
 
o
r
g
a
n
i
z
e
d
 
a
s
 
a
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
h
t
m
l
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
 
H
T
M
L
 
c
o
n
t
e
n
t
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
:
 
A
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
f
 
s
t
r
i
n
g
s
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
t
a
b
l
e
 
d
a
t
a
.


 
 
 
 
"
"
"


 
 
 
 
f
r
o
m
 
b
s
4
 
i
m
p
o
r
t
 
B
e
a
u
t
i
f
u
l
S
o
u
p


 
 
 
 
s
o
u
p
 
=
 
B
e
a
u
t
i
f
u
l
S
o
u
p
(
h
t
m
l
_
c
o
n
t
e
n
t
,
 
'
h
t
m
l
.
p
a
r
s
e
r
'
)


 
 
 
 
t
a
b
l
e
_
d
a
t
a
 
=
 
[
]


 
 
 
 
f
o
r
 
t
a
b
l
e
 
i
n
 
s
o
u
p
.
f
i
n
d
_
a
l
l
(
'
t
a
b
l
e
'
)
:


 
 
 
 
 
 
 
 
t
a
b
l
e
_
d
a
t
a
.
a
p
p
e
n
d
(
[
]
)


 
 
 
 
 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
t
a
b
l
e
.
f
i
n
d
_
a
l
l
(
'
t
r
'
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
_
d
a
t
a
 
=
 
[
]


 
 
 
 
 
 
 
 
 
 
 
 
f
o
r
 
c
e
l
l
 
i
n
 
r
o
w
.
f
i
n
d
_
a
l
l
(
[
'
t
d
'
,
 
'
t
h
'
]
)
:


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
_
d
a
t
a
.
a
p
p
e
n
d
(
c
e
l
l
.
t
e
x
t
.
s
t
r
i
p
(
)
)


 
 
 
 
 
 
 
 
 
 
 
 
t
a
b
l
e
_
d
a
t
a
[
-
1
]
.
a
p
p
e
n
d
(
r
o
w
_
d
a
t
a
)


 
 
 
 
r
e
t
u
r
n
 
t
a
b
l
e
_
d
a
t
a






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
c
s
v
_
d
a
t
a
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
L
i
s
t
[
s
t
r
]
]
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
 
t
a
b
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
 
f
r
o
m
 
a
 
f
i
l
e
 
p
a
t
h
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
q
u
e
s
t
i
o
n
 
o
r
g
a
n
i
z
e
d
 
a
s
 
a
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
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
 
p
a
t
h
 
t
o
 
t
h
e
 
H
T
M
L
 
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


 
 
 
 
 
 
 
 
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
:
 
A
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
f
 
s
t
r
i
n
g
s
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
t
a
b
l
e
 
d
a
t
a
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
i
l
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
e
x
t
r
a
c
t
_
c
s
v
_
d
a
t
a
_
f
r
o
m
_
h
t
m
l
(
f
i
l
e
.
r
e
a
d
(
)
)






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
c
s
v
_
d
a
t
a
_
f
r
o
m
_
u
r
l
(
u
r
l
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
L
i
s
t
[
s
t
r
]
]
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
 
t
a
b
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
 
f
r
o
m
 
a
 
U
R
L
 
a
n
d
 
r
e
t
u
r
n
 
t
h
e
 
q
u
e
s
t
i
o
n
 
o
r
g
a
n
i
z
e
d
 
a
s
 
a
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
.




 
 
 
 
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
 
U
R
L
 
t
o
 
t
h
e
 
H
T
M
L
 
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


 
 
 
 
 
 
 
 
L
i
s
t
[
L
i
s
t
[
s
t
r
]
]
:
 
A
 
t
w
o
-
d
i
m
e
n
s
i
o
n
a
l
 
a
r
r
a
y
 
o
f
 
s
t
r
i
n
g
s
 
r
e
p
r
e
s
e
n
t
i
n
g
 
t
h
e
 
t
a
b
l
e
 
d
a
t
a
.


 
 
 
 
"
"
"


 
 
 
 
i
m
p
o
r
t
 
r
e
q
u
e
s
t
s


 
 
 
 
r
e
s
p
o
n
s
e
 
=
 
r
e
q
u
e
s
t
s
.
g
e
t
(
u
r
l
)


 
 
 
 
r
e
t
u
r
n
 
e
x
t
r
a
c
t
_
c
s
v
_
d
a
t
a
_
f
r
o
m
_
h
t
m
l
(
r
e
s
p
o
n
s
e
.
t
e
x
t
)






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
c
s
v
_
d
a
t
a
_
f
r
o
m
_
u
r
l
_
f
i
l
e
(
import unittest


class TestHTMLToCSVExtraction(unittest.TestCase):

    def test_table_with_multiple_rows_and_columns(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Cell 1</td><td>Cell 2</td></tr>
                <tr><td>Cell 3</td><td>Cell 4</td></tr>
            </tbody>
        </table>
        """
        expected = [["Cell 1", "Cell 2"], ["Cell 3", "Cell 4"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_empty_cells(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Cell 1</td><td></td></tr>
                <tr><td></td><td>Cell 4</td></tr>
            </tbody>
        </table>
        """
        expected = [["Cell 1", ""], ["", "Cell 4"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_only_one_row(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Single Cell 1</td><td>Single Cell 2</td></tr>
            </tbody>
        </table>
        """
        expected = [["Single Cell 1", "Single Cell 2"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_table_with_only_one_column(self):
        test_case_html = """
        <table class="waffle">
            <tbody>
                <tr><td>Column Cell 1</td></tr>
                <tr><td>Column Cell 2</td></tr>
            </tbody>
        </table>
        """
        expected = [["Column Cell 1"], ["Column Cell 2"]]
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

    def test_no_table_with_class_waffle_present(self):
        test_case_html = """
        <div>
            <p>No table here!</p>
        </div>
        """
        expected = []
        self.assertEqual(extract_csv_data_from_html(test_case_html), expected)

if __name__ == '__main__':
    unittest.main()