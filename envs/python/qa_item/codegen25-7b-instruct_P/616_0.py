d
e
f
 
b
y
t
e
_
c
o
u
n
t
_
t
o
_
d
i
s
p
l
a
y
_
s
i
z
e
(
s
i
z
e
_
i
n
_
b
y
t
e
s
:
 
i
n
t
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
C
o
n
v
e
r
t
s
 
a
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
t
o
 
a
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
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
a
t
i
o
n
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
i
z
e
_
i
n
_
b
y
t
e
s
 
(
i
n
t
)
:
 
T
h
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
t
o
 
c
o
n
v
e
r
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
 
r
e
p
r
e
s
e
n
t
a
t
i
o
n
 
o
f
 
t
h
e
 
s
i
z
e
 
i
n
 
a
n
 
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
 
u
n
i
t
 
(
b
y
t
e
s
,
 
K
B
,
 
M
B
,
 
G
B
,
 
T
B
)
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
s
i
z
e
_
i
n
_
b
y
t
e
s
 
<
 
1
0
2
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
s
i
z
e
_
i
n
_
b
y
t
e
s
}
 
B
"


 
 
 
 
e
l
i
f
 
s
i
z
e
_
i
n
_
b
y
t
e
s
 
<
 
1
0
2
4
 
*
*
 
2
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
r
o
u
n
d
(
s
i
z
e
_
i
n
_
b
y
t
e
s
 
/
 
1
0
2
4
,
 
2
)
}
 
K
B
"


 
 
 
 
e
l
i
f
 
s
i
z
e
_
i
n
_
b
y
t
e
s
 
<
 
1
0
2
4
 
*
*
 
3
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
r
o
u
n
d
(
s
i
z
e
_
i
n
_
b
y
t
e
s
 
/
 
1
0
2
4
 
*
*
 
2
,
 
2
)
}
 
M
B
"


 
 
 
 
e
l
i
f
 
s
i
z
e
_
i
n
_
b
y
t
e
s
 
<
 
1
0
2
4
 
*
*
 
4
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
r
o
u
n
d
(
s
i
z
e
_
i
n
_
b
y
t
e
s
 
/
 
1
0
2
4
 
*
*
 
3
,
 
2
)
}
 
G
B
"


 
 
 
 
e
l
s
e
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
f
"
{
r
o
u
n
d
(
s
i
z
e
_
i
n
_
b
y
t
e
s
 
/
 
1
0
2
4
 
*
*
 
4
,
 
2
)
}
 
T
B
"






d
e
f
 
d
i
s
p
l
a
y
_
s
i
z
e
_
t
o
_
b
y
t
e
_
c
o
u
n
t
(
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
:
 
s
t
r
)
 
-
>
 
i
n
t
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
s
 
a
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
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
a
t
i
o
n
 
o
f
 
a
 
s
i
z
e
 
i
n
 
b
y
t
e
s
 
t
o
 
a
n
 
i
n
t
e
g
e
r
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
 
(
s
t
r
)
:
 
T
h
e
 
s
i
z
e
 
i
n
 
h
u
m
a
n
-
r
e
a
d
a
b
l
e
 
u
n
i
t
s
 
(
b
y
t
e
s
,
 
K
B
,
 
M
B
,
 
G
B
,
 
T
B
)
.




 
 
 
 
R
e
t
u
r
n
s
:


 
 
 
 
 
 
 
 
i
n
t
:
 
T
h
e
 
s
i
z
e
 
i
n
 
b
y
t
e
s
.


 
 
 
 
"
"
"


 
 
 
 
i
f
 
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
.
e
n
d
s
w
i
t
h
(
"
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
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
B
"
,
 
"
"
)
)


 
 
 
 
e
l
i
f
 
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
.
e
n
d
s
w
i
t
h
(
"
K
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
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
K
B
"
,
 
"
"
)
)
 
*
 
1
0
2
4
)


 
 
 
 
e
l
i
f
 
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
.
e
n
d
s
w
i
t
h
(
"
M
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
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
M
B
"
,
 
"
"
)
)
 
*
 
1
0
2
4
 
*
*
 
2
)


 
 
 
 
e
l
i
f
 
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
.
e
n
d
s
w
i
t
h
(
"
G
B
"
)
:


 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
n
t
(
f
l
o
a
t
(
s
i
z
e
_
i
n
_
d
i
s
p
l
a
y
_
u
n
i
t
s
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
G
B
"
,
 
"
"
)
)
import unittest


class TestByteCountToDisplaySizeByteCountToDisplaySize(unittest.TestCase):

    def test_zero_bytes(self):
        """Test case for 0 bytes."""
        input_size = 0
        expected = "0 bytes"
        self.assertEqual(byte_count_to_display_size(input_size), expected)

    def test_bytes_less_than_kb(self):
        """Test case for bytes less than 1KB."""
        input_size = 500
        expected = "500 bytes"
        self.assertEqual(byte_count_to_display_size(input_size), expected)

    def test_exactly_one_kb(self):
        """Test case for exactly 1KB."""
        input_size = 1024
        result = byte_count_to_display_size(input_size)
        self.assertTrue(result == "1 KB" or result == "1.00 KB")

    def test_between_kb_and_mb(self):
        """Test case for a size between 1KB and 1MB."""
        input_size = 5000
        expected = "4.88 KB"
        self.assertEqual(byte_count_to_display_size(input_size), expected)

    def test_exactly_one_mb(self):
        """Test case for exactly 1MB."""
        input_size = 1048576  # 1024 * 1024
        result = byte_count_to_display_size(input_size)
        self.assertTrue(result == "1 MB" or result == "1.00 MB")

if __name__ == '__main__':
    unittest.main()