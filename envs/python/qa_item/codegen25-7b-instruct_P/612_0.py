d
e
f
 
f
i
n
d
_
a
n
d
_
r
e
p
l
a
c
e
_
i
n
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
,
 
s
e
a
r
c
h
_
s
t
r
i
n
g
:
s
t
r
,
 
r
e
p
l
a
c
e
_
s
t
r
i
n
g
:
s
t
r
)
:


 
 
 
 
"
"
"


 
 
 
 
F
i
n
d
s
 
a
n
d
 
r
e
p
l
a
c
e
s
 
t
e
x
t
 
i
n
 
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
 
T
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
 
f
i
l
e
.


 
 
 
 
 
 
 
 
s
e
a
r
c
h
_
s
t
r
i
n
g
 
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
t
r
i
n
g
 
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
.


 
 
 
 
 
 
 
 
r
e
p
l
a
c
e
_
s
t
r
i
n
g
 
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
t
r
i
n
g
 
t
o
 
r
e
p
l
a
c
e
 
w
i
t
h
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
I
O
E
r
r
o
r
:
 
I
f
 
a
n
 
I
/
O
 
e
r
r
o
r
 
o
c
c
u
r
s
 
r
e
a
d
i
n
g
 
f
r
o
m
 
t
h
e
 
f
i
l
e
 
o
r
 
w
r
i
t
i
n
g
 
t
o
 
t
h
e
 
f
i
l
e
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
+
'
)
 
a
s
 
f
i
l
e
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
s
 
=
 
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
s
 
=
 
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
s
e
a
r
c
h
_
s
t
r
i
n
g
,
 
r
e
p
l
a
c
e
_
s
t
r
i
n
g
)


 
 
 
 
 
 
 
 
f
i
l
e
.
s
e
e
k
(
0
)


 
 
 
 
 
 
 
 
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
s
)


 
 
 
 
 
 
 
 
f
i
l
e
.
t
r
u
n
c
a
t
e
(
)




d
e
f
 
g
e
t
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
s
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
 
s
t
r
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
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
s
 
o
f
 
a
 
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
 
T
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


 
 
 
 
 
 
 
 
s
t
r
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
s
 
o
f
 
t
h
e
 
f
i
l
e
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
I
O
E
r
r
o
r
:
 
I
f
 
a
n
 
I
/
O
 
e
r
r
o
r
 
o
c
c
u
r
s
 
r
e
a
d
i
n
g
 
f
r
o
m
 
t
h
e
 
f
i
l
e
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




d
e
f
 
g
e
t
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
s
_
a
s
_
l
i
s
t
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
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
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
s
 
o
f
 
a
 
f
i
l
e
 
a
s
 
a
 
l
i
s
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
 
T
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


 
 
 
 
 
 
 
 
l
i
s
t
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
s
 
o
f
 
t
h
e
 
f
i
l
e
 
a
s
 
a
 
l
i
s
t
.




 
 
 
 
R
a
i
s
e
s
:


 
 
 
 
 
 
 
 
I
O
E
r
r
o
r
:
 
I
f
 
a
n
 
I
/
O
 
e
r
r
o
r
 
o
c
c
u
r
s
 
r
e
a
d
i
n
g
 
f
r
o
m
 
t
h
e
 
f
i
l
e
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
 
f
i
l
e
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




d
e
f
 
g
e
t
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
s
_
a
s
_
l
i
s
t
_
o
f
_
s
t
r
i
n
g
s
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
 
l
i
s
t
:


 
 
 
 
"
"
"


 
 
 
 
G
e
t
s
 
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
s
 
o
f
 
a
 
f
i
l
e
 
a
s
 
a
 
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
 
T
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


 
 
 
 
 
 
 
 
l
i
s
t
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
s
 
o
f
 
t
h
e
 
f
i
l
e
 
a
s
 
a
 
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
.
import os
import unittest


class TestFindAndReplace(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for the tests
        self.temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
        os.makedirs(self.temp_dir, exist_ok=True)

    def tearDown(self):
        # Remove the temporary directory after tests
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

    # Test case 1: Basic find and replace
    def test_find_and_replace_basic(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "World", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello Java\n", "Goodbye Java\n"])

    # Test case 2: No occurrences of the search string
    def test_find_and_replace_no_occurrences(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "Python", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello World\n", "Goodbye World\n"])

    # Test case 3: Multiple occurrences in a single line
    def test_find_and_replace_multiple_occurrences(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "World", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello Java Java\n", "Goodbye Java\n"])

    # Test case 4: Replace with an empty string
    def test_find_and_replace_with_empty_string(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["Hello World\n", "Goodbye World\n"])

        find_and_replace_in_file(file_path, "World", "")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["Hello \n", "Goodbye \n"])

    # Test case 5: Empty file
    def test_find_and_replace_empty_file(self):
        file_path = os.path.join(self.temp_dir, "testfile.txt")
        with open(file_path, 'w') as file:
            file.writelines(["\n"])

        find_and_replace_in_file(file_path, "World", "Java")

        with open(file_path, 'r') as file:
            result = file.readlines()

        self.assertEqual(result, ["\n"])

if __name__ == '__main__':
    unittest.main()