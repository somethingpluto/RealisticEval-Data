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
 
c
o
n
v
e
r
t
_
d
a
t
a
f
r
a
m
e
_
t
o
_
m
a
r
k
d
o
w
n
(
d
f
:
 
p
d
.
D
a
t
a
F
r
a
m
e
,
 
m
d
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
a
 
D
a
t
a
F
r
a
m
e
 
o
b
j
e
c
t
 
t
o
 
a
 
t
a
b
l
e
 
i
n
 
m
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


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
d
a
t
a
f
r
a
m
e
 
{
'
N
a
m
e
'
:
 
[
'
A
l
i
c
e
'
,
 
'
B
o
b
'
]
,
 
'
A
g
e
'
:
 
[
2
5
,
 
3
0
]
}


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
|
 
N
a
m
e
 
|
 
A
g
e
 
|
\
n
|
 
-
-
-
 
|
 
-
-
-
 
|
\
n
|
 
A
l
i
c
e
 
|
 
2
5
 
|
\
n
|
 
B
o
b
 
|
 
3
0
 
|
\
n




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
f
 
(
D
a
t
a
F
r
a
m
e
)
:
 
D
a
t
a
F
r
a
m
e
 
t
y
p
e
 
q
u
e
s
t
i
o
n


 
 
 
 
 
 
 
 
m
d
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
 
o
u
t
p
u
t
 
m
d
 
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


 
 
 
 
 
 
 
 
m
a
r
k
d
o
w
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
 
s
t
r


 
 
 
 
"
"
"


 
 
 
 
m
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
 
"
|
 
"


 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
:


 
 
 
 
 
 
 
 
m
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
 
c
o
l
 
+
 
"
 
|
 
"


 
 
 
 
m
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
 
"
\
n
|
 
"


 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
:


 
 
 
 
 
 
 
 
m
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
 
"
 
-
-
-
 
|
 
"


 
 
 
 
m
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
 
"
\
n
"


 
 
 
 
f
o
r
 
_
,
 
r
o
w
 
i
n
 
d
f
.
i
t
e
r
r
o
w
s
(
)
:


 
 
 
 
 
 
 
 
m
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
 
"
|
 
"


 
 
 
 
 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
:


 
 
 
 
 
 
 
 
 
 
 
 
m
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
 
s
t
r
(
r
o
w
[
c
o
l
]
)
 
+
 
"
 
|
 
"


 
 
 
 
 
 
 
 
m
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
 
"
\
n
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
m
d
_
p
a
t
h
,
 
"
w
"
)
 
a
s
 
f
:


 
 
 
 
 
 
 
 
f
.
w
r
i
t
e
(
m
d
_
c
o
n
t
e
n
t
)


 
 
 
 
r
e
t
u
r
n
 
m
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
 
c
o
n
v
e
r
t
_
d
a
t
a
f
r
a
m
e
_
t
o
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
w
i
t
h
_
i
n
d
e
x
(
d
f
:
 
p
d
.
D
a
t
a
F
r
a
m
e
,
 
m
d
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
c
o
n
v
e
r
t
 
a
 
D
a
t
a
F
r
a
m
e
 
o
b
j
e
c
t
 
t
o
 
a
 
t
a
b
l
e
 
i
n
 
m
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


 
 
 
 
F
o
r
 
e
x
a
m
p
l
e
:


 
 
 
 
 
 
 
 
i
n
p
u
t
:
 
d
a
t
a
f
r
a
m
e
 
{
'
N
a
m
e
'
:
 
[
'
A
l
i
c
e
'
,
 
'
B
o
b
'
]
,
 
'
A
g
e
'
:
 
[
2
5
,
 
3
0
]
}


 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
|
 
N
a
m
e
 
|
 
A
g
e
 
|
\
n
|
 
-
-
-
 
|
 
-
-
-
 
|
\
n
|
 
A
l
i
c
e
 
|
 
2
5
 
|
\
n
|
 
B
o
b
 
|
 
3
0
 
|
\
n




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
d
f
 
(
D
a
t
a
F
r
a
m
e
)
:
 
D
a
t
a
F
r
a
m
e
 
t
y
p
e
 
q
u
e
s
t
i
o
n


 
 
 
 
 
 
 
 
m
d
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
 
o
u
t
p
u
t
 
m
d
 
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


 
 
 
 
 
 
 
 
m
a
r
k
d
o
w
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
 
s
t
r


 
 
 
 
"
"
"


 
 
 
 
m
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
 
"
|
 
"


 
 
 
 
f
o
r
 
c
o
l
 
i
n
 
d
f
.
c
o
l
u
m
n
s
:


 
 
 
 
 
 
 
 
m
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
 
c
o
l
 
+
 
"
 
|
 
"


 
 
 
 
m
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
 
"
\
n
|
 
"


 
 
 
 
f
o
r
 
c
o
l
import unittest
=import pandas as pd


class TestDataframeToMarkdown(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame
        self.data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        self.df = pd.DataFrame(self.data)

    def test_df_to_str(self):
        # Test that the function writes the correct markdown to a file
        expected_markdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    25 |\n| Bob    |    30 |"
        result = convert_dataframe_to_markdown(self.df, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_empty_dataframe(self):
        # Test how the function handles an empty DataFrame
        df_empty = pd.DataFrame()
        expected_markdown = ""
        result = convert_dataframe_to_markdown(df_empty, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_single_row_dataframe(self):
        # Test with a DataFrame that contains only one row
        df_single_row = pd.DataFrame({'Name': ['Alice'], 'Age': [30]})
        expected_markdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    30 |"
        result = convert_dataframe_to_markdown(df_single_row, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_non_string_columns(self):
        # Test with non-string question types in the DataFrame
        df_non_string = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30], 'Height': [5.5, 6.0]})
        expected_markdown = ('| Name   |   Age |   Height |\n'
                             '|:-------|------:|---------:|\n'
                             '| Alice  |    25 |      5.5 |\n'
                             '| Bob    |    30 |      6   |')
        result = convert_dataframe_to_markdown(df_non_string, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)

    def test_special_characters(self):
        # Test handling of special characters in DataFrame
        df_special_chars = pd.DataFrame(
            {'Name': ['Alice', 'Bob'], 'Comments': ['Good@Work!', 'Excellent & Commendable']})
        expected_markdown = ('| Name   | Comments                |\n'
                             '|:-------|:------------------------|\n'
                             '| Alice  | Good@Work!              |\n'
                             '| Bob    | Excellent & Commendable |')
        result = convert_dataframe_to_markdown(df_special_chars, 'dummy_path.md')
        self.assertEqual(result, expected_markdown)


if __name__ == '__main__':
    unittest.main()