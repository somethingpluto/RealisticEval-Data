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
 
p
a
r
s
e
_
m
a
r
k
d
o
w
n
_
t
a
b
l
e
(
m
d
_
t
a
b
l
e
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
t
u
p
l
e
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
 
M
a
r
k
d
o
w
n
 
f
o
r
m
a
t
t
e
d
 
t
a
b
l
e
 
i
n
t
o
 
a
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
,
 
e
a
c
h
 
t
u
p
l
e
 
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
 
a
 
r
o
w
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
d
_
t
a
b
l
e
 
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
 
a
 
M
a
r
k
d
o
w
n
 
t
a
b
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


 
 
 
 
 
 
 
 
l
i
s
t
 
o
f
 
t
u
p
l
e
s
:
 
A
 
l
i
s
t
 
w
h
e
r
e
 
e
a
c
h
 
t
u
p
l
e
 
r
e
p
r
e
s
e
n
t
s
 
a
 
r
o
w
 
i
n
 
t
h
e
 
t
a
b
l
e
.


 
 
 
 
"
"
"


 
 
 
 
r
o
w
s
 
=
 
m
d
_
t
a
b
l
e
.
s
p
l
i
t
(
"
\
n
"
)


 
 
 
 
t
a
b
l
e
 
=
 
[
]


 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
r
o
w
s
:


 
 
 
 
 
 
 
 
i
f
 
r
o
w
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
|
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
 
=
 
r
o
w
.
r
e
p
l
a
c
e
(
"
|
"
,
 
"
"
,
 
1
)


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
 
=
 
r
o
w
.
r
e
p
l
a
c
e
(
"
|
"
,
 
"
"
,
 
-
1
)


 
 
 
 
 
 
 
 
 
 
 
 
t
a
b
l
e
.
a
p
p
e
n
d
(
t
u
p
l
e
(
r
o
w
.
s
p
l
i
t
(
"
|
"
)
)
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






d
e
f
 
p
a
r
s
e
_
m
a
r
k
d
o
w
n
_
t
a
b
l
e
_
t
o
_
d
i
c
t
(
m
d
_
t
a
b
l
e
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
d
i
c
t
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
 
M
a
r
k
d
o
w
n
 
f
o
r
m
a
t
t
e
d
 
t
a
b
l
e
 
i
n
t
o
 
a
 
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
,
 
e
a
c
h
 
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
 
a
 
r
o
w
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
d
_
t
a
b
l
e
 
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
 
a
 
M
a
r
k
d
o
w
n
 
t
a
b
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
s
:
 
A
 
l
i
s
t
 
w
h
e
r
e
 
e
a
c
h
 
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
 
r
e
p
r
e
s
e
n
t
s
 
a
 
r
o
w
 
i
n
 
t
h
e
 
t
a
b
l
e
.


 
 
 
 
"
"
"


 
 
 
 
r
o
w
s
 
=
 
m
d
_
t
a
b
l
e
.
s
p
l
i
t
(
"
\
n
"
)


 
 
 
 
t
a
b
l
e
 
=
 
[
]


 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
r
o
w
s
:


 
 
 
 
 
 
 
 
i
f
 
r
o
w
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
|
"
)
:


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
 
=
 
r
o
w
.
r
e
p
l
a
c
e
(
"
|
"
,
 
"
"
,
 
1
)


 
 
 
 
 
 
 
 
 
 
 
 
r
o
w
 
=
 
r
o
w
.
r
e
p
l
a
c
e
(
"
|
"
,
 
"
"
,
 
-
1
)


 
 
 
 
 
 
 
 
 
 
 
 
t
a
b
l
e
.
a
p
p
e
n
d
(
d
i
c
t
(
z
i
p
(
t
a
b
l
e
[
0
]
,
 
r
o
w
.
s
p
l
i
t
(
"
|
"
)
)
)
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






d
e
f
 
p
a
r
s
e
_
m
a
r
k
d
o
w
n
_
t
a
b
l
e
_
t
o
_
d
i
c
t
_
o
f
_
l
i
s
t
s
(
m
d
_
t
a
b
l
e
:
 
s
t
r
)
 
-
>
 
d
i
c
t
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
 
M
a
r
k
d
o
w
n
 
f
o
r
m
a
t
t
e
d
 
t
a
b
l
e
 
i
n
t
o
 
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
 
o
f
 
l
i
s
t
s
,
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
i
s
 
a
 
c
o
l
u
m
n
 
n
a
m
e
 
a
n
d
 
e
a
c
h
 
v
a
l
u
e
 
i
s
 
a
 
l
i
s
t
 
o
f
 
c
o
l
u
m
n
 
v
a
l
u
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
d
_
t
a
b
l
e
 
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
 
a
 
M
a
r
k
d
o
w
n
 
t
a
b
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


 
 
 
 
 
 
 
 
d
i
c
t
 
o
f
 
l
i
s
t
s
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
 
w
h
e
r
e
 
e
a
c
h
 
k
e
y
 
i
s
 
a
 
c
o
l
u
m
n
 
n
a
m
e
 
a
n
d
 
e
a
c
h
 
v
a
l
u
e
 
i
s
 
a
 
l
i
s
t
 
o
f
 
c
o
l
u
m
n
 
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
o
w
s
 
=
 
m
d
_
t
a
b
l
e
.
s
p
l
i
t
(
"
\
n
"
)


 
 
 
 
t
a
b
l
e
 
=
 
{
}


 
 
 
 
f
o
r
 
r
o
w
 
i
n
 
r
o
w
s
:
import unittest


class TestParseMarkdownTable(unittest.TestCase):
    def test_standard_table(self):
        md_table = """
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        | Row1Col1 | Row1Col2 | Row1Col3 |
        | Row2Col1 | Row2Col2 | Row2Col3 |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('Row1Col1', 'Row1Col2', 'Row1Col3'),
            ('Row2Col1', 'Row2Col2', 'Row2Col3')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_inconsistent_columns(self):
        md_table = """
        | Header 1 | Header 2 |
        |----------|----------|
        | Row1     | Row1Col2 | ExtraCol |
        | Row2     |
        """
        expected = [
            ('Header 1', 'Header 2'),
            ('Row1', 'Row1Col2', 'ExtraCol'),
            ('Row2',)
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_empty_cells(self):
        md_table = """
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          | Row1Col2 |          |
        | Row2Col1 |          | Row2Col3 |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('', 'Row1Col2', ''),
            ('Row2Col1', '', 'Row2Col3')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_all_empty_rows(self):
        md_table = """
        | Header 1 | Header 2 | Header 3 |
        |----------|----------|----------|
        |          |          |          |
        |          |          |          |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('', '', ''),
            ('', '', '')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)

    def test_excessive_whitespace(self):
        md_table = """
        |  Header 1  |  Header 2  |  Header 3  |
        |------------|------------|------------|
        |  Row1Col1  |  Row1Col2  |  Row1Col3  |
        |  Row2Col1  |  Row2Col2  |  Row2Col3  |
        """
        expected = [
            ('Header 1', 'Header 2', 'Header 3'),
            ('Row1Col1', 'Row1Col2', 'Row1Col3'),
            ('Row2Col1', 'Row2Col2', 'Row2Col3')
        ]
        result = parse_markdown_table(md_table)
        self.assertEqual(result, expected)


def parse_markdown_table(md_table):
    """
    Parses a Markdown formatted table into a list of tuples, each tuple representing a row.

    Args:
        md_table (str): A string representing a Markdown table.

    Returns:
        list of tuples: A list where each tuple represents a row in the table.
    """
    # Split the input string into lines and strip whitespace
    lines = md_table.strip().split('\n')

    # Filter out the separator line for the header (which usually contains "---")
    lines = [line for line in lines if not line.strip().startswith('|---')]

    # Initialize the list to store each row as a tuple
    table_data = []

    # Process each line
    for line in lines:
        # Strip leading and trailing spaces and pipes, then split by "|"
        row = line.strip('| \n').split('|')
        # Strip spaces from each cell, handle empty cells, and create a tuple
        table_data.append(tuple(cell.strip() for cell in row if cell.strip() or cell == ''))

    return table_data

if __name__ == '__main__':
    unittest.main()