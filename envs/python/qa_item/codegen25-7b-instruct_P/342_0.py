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
i
t
l
e
s
(
m
a
r
k
d
o
w
n
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


 
 
 
 
P
a
r
s
e
s
 
m
a
r
k
d
o
w
n
 
t
e
x
t
 
t
o
 
e
x
t
r
a
c
t
 
t
i
t
l
e
s
 
o
f
 
d
i
f
f
e
r
e
n
t
 
l
e
v
e
l
s
.




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
t
a
k
e
s
 
a
 
s
t
r
i
n
g
 
o
f
 
m
a
r
k
d
o
w
n
 
c
o
n
t
e
n
t
 
a
s
 
i
n
p
u
t
 
a
n
d
 
r
e
t
u
r
n
s
 
a
n


 
 
 
 
o
b
j
e
c
t
 
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
r
r
a
y
s
 
o
f
 
t
i
t
l
e
s
 
c
a
t
e
g
o
r
i
z
e
d
 
b
y
 
t
h
e
i
r
 
l
e
v
e
l
:


 
 
 
 
l
e
v
e
l
 
1
 
(
H
1
)
,
 
l
e
v
e
l
 
2
 
(
H
2
)
,
 
a
n
d
 
l
e
v
e
l
 
3
 
(
H
3
)
.




 
 
 
 
A
r
g
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
t
e
d
 
t
e
x
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
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
i
t
h
 
t
h
r
e
e
 
p
r
o
p
e
r
t
i
e
s
:
 
l
e
v
e
l
1
,
 
l
e
v
e
l
2
,
 
a
n
d
 
l
e
v
e
l
3
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
a
c
h
 
h
o
l
d
i
n
g
 
a
 
l
i
s
t
 
o
f
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
t
i
t
l
e
s
 
f
o
u
n
d
 
i
n
 
t
h
e
 
m
a
r
k
d
o
w
n
.


 
 
 
 
"
"
"


 
 
 
 
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
 
t
o
 
h
o
l
d
 
t
h
e
 
t
i
t
l
e
s


 
 
 
 
t
i
t
l
e
s
 
=
 
{


 
 
 
 
 
 
 
 
"
l
e
v
e
l
1
"
:
 
[
]
,


 
 
 
 
 
 
 
 
"
l
e
v
e
l
2
"
:
 
[
]
,


 
 
 
 
 
 
 
 
"
l
e
v
e
l
3
"
:
 
[
]
,


 
 
 
 
}




 
 
 
 
#
 
S
p
l
i
t
 
t
h
e
 
m
a
r
k
d
o
w
n
 
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
 
m
a
r
k
d
o
w
n
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




 
 
 
 
#
 
I
t
e
r
a
t
e
 
o
v
e
r
 
t
h
e
 
l
i
n
e
s


 
 
 
 
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
i
n
e
s
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
 
i
s
 
a
 
t
i
t
l
e


 
 
 
 
 
 
 
 
i
f
 
l
i
n
e
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
#
"
)
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
 
t
i
t
l
e
 
l
e
v
e
l


 
 
 
 
 
 
 
 
 
 
 
 
l
e
v
e
l
 
=
 
l
e
n
(
l
i
n
e
)
 
-
 
l
e
n
(
l
i
n
e
.
l
s
t
r
i
p
(
"
#
"
)
)




 
 
 
 
 
 
 
 
 
 
 
 
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
 
t
i
t
l
e
 
t
e
x
t


 
 
 
 
 
 
 
 
 
 
 
 
t
i
t
l
e
 
=
 
l
i
n
e
.
l
s
t
r
i
p
(
"
#
"
)
.
s
t
r
i
p
(
)




 
 
 
 
 
 
 
 
 
 
 
 
#
 
A
d
d
 
t
h
e
 
t
i
t
l
e
 
t
o
 
t
h
e
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
l
i
s
t


 
 
 
 
 
 
 
 
 
 
 
 
t
i
t
l
e
s
[
f
"
l
e
v
e
l
{
l
e
v
e
l
}
"
]
.
a
p
p
e
n
d
(
t
i
t
l
e
)




 
 
 
 
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
 
t
i
t
l
e
s


 
 
 
 
r
e
t
u
r
n
 
t
i
t
l
e
s






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
s
e
c
t
i
o
n
s
(
m
a
r
k
d
o
w
n
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


 
 
 
 
P
a
r
s
e
s
 
m
a
r
k
d
o
w
n
 
t
e
x
t
 
t
o
 
e
x
t
r
a
c
t
 
s
e
c
t
i
o
n
s
 
o
f
 
d
i
f
f
e
r
e
n
t
 
l
e
v
e
l
s
.




 
 
 
 
T
h
i
s
 
f
u
n
c
t
i
o
n
 
t
a
k
e
s
 
a
 
s
t
r
i
n
g
 
o
f
 
m
a
r
k
d
o
w
n
 
c
o
n
t
e
n
t
 
a
s
 
i
n
p
u
t
 
a
n
d
 
r
e
t
u
r
n
s
 
a
n


 
 
 
 
o
b
j
e
c
t
 
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
r
r
a
y
s
 
o
f
 
s
e
c
t
i
o
n
s
 
c
a
t
e
g
o
r
i
z
e
d
 
b
y
 
t
h
e
i
r
 
l
e
v
e
l
:


 
 
 
 
l
e
v
e
l
 
1
 
(
H
1
)
,
 
l
e
v
e
l
 
2
 
(
H
2
)
,
 
a
n
d
 
l
e
v
e
l
 
3
 
(
H
3
)
.




 
 
 
 
A
r
g
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
t
e
d
 
t
e
x
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


 
 
 
 
 
 
 
 
D
i
c
t
[
s
t
r
,
 
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
i
t
h
 
t
h
r
e
e
 
p
r
o
p
e
r
t
i
e
s
:
 
l
e
v
e
l
1
,
 
l
e
v
e
l
2
,
 
a
n
d
 
l
e
v
e
l
3
,


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
a
c
h
 
h
o
l
d
i
n
g
 
a
 
l
i
s
t
 
o
f
 
c
o
r
r
e
s
p
o
n
d
i
n
g
 
s
e
c
t
i
o
n
s
 
f
o
u
n
d
 
i
n
 
t
h
e
 
m
a
r
k
d
o
w
n
.
import unittest


class TestParseMarkdownTitles(unittest.TestCase):

    def test_extract_first_second_and_third_level_titles(self):
        markdown = """        
        # Title 1
        Content here.
        ## Subtitle 1.1
        More content.
        ### Subsubtitle 1.1.1
        Even more content.
        # Title 2
        Another content.
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Title 1", "Title 2"],
            'level2': ["Subtitle 1.1"],
            'level3': ["Subsubtitle 1.1.1"],
        })

    def test_handle_missing_headers(self):
        markdown = """        
        This is just some text without headers.
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': [],
            'level2': [],
            'level3': [],
        })

    def test_handle_only_first_level_headers(self):
        markdown = """        
        # Only Title 1
        Content without subtitles.

        # Only Title 2
        More content.
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Only Title 1", "Only Title 2"],
            'level2': [],
            'level3': [],
        })

    def test_handle_mixed_headers_with_empty_lines(self):
        markdown = """        
        # Title 1
        ## Subtitle 1.1
        Some content here.
        ### Subsubtitle 1.1.1

        # Title 2
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Title 1", "Title 2"],
            'level2': ["Subtitle 1.1"],
            'level3': ["Subsubtitle 1.1.1"],
        })

    def test_handle_headers_with_special_characters(self):
        markdown = """        
        # Title 1 - Special Characters!
        ## Subtitle 1.1: The Beginning
        ### Subsubtitle 1.1.1 (Note)
        """
        result = parse_markdown_titles(markdown)
        self.assertEqual(result, {
            'level1': ["Title 1 - Special Characters!"],
            'level2': ["Subtitle 1.1: The Beginning"],
            'level3': ["Subsubtitle 1.1.1 (Note)"],
        })

if __name__ == '__main__':
    unittest.main()