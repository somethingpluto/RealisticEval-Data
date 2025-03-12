c
l
a
s
s
 
C
o
l
o
r
s
:




 
 
 
 
@
s
t
a
t
i
c
m
e
t
h
o
d


 
 
 
 
d
e
f
 
r
e
d
(
t
e
x
t
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
t
e
x
t
 
i
n
 
r
e
d
 
c
o
l
o
r
"
"
"


 
 
 
 
 
 
 
 
p
a
s
s




 
 
 
 
@
s
t
a
t
i
c
m
e
t
h
o
d


 
 
 
 
d
e
f
 
g
r
e
e
n
(
t
e
x
t
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
t
e
x
t
 
i
n
 
g
r
e
e
n
 
c
o
l
o
r
"
"
"




 
 
 
 
@
s
t
a
t
i
c
m
e
t
h
o
d


 
 
 
 
d
e
f
 
b
l
u
e
(
t
e
x
t
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
t
e
x
t
 
i
n
 
b
l
u
e
 
c
o
l
o
r
"
"
"




 
 
 
 
@
s
t
a
t
i
c
m
e
t
h
o
d


 
 
 
 
d
e
f
 
y
e
l
l
o
w
(
t
e
x
t
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
t
e
x
t
 
i
n
 
y
e
l
l
o
w
 
c
o
l
o
r
"
"
"




 
 
 
 
@
s
t
a
t
i
c
m
e
t
h
o
d


 
 
 
 
d
e
f
 
m
a
g
e
n
t
a
(
t
e
x
t
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
t
e
x
t
 
i
n
 
m
a
g
e
n
t
a
 
c
o
l
o
r
"
"
"




 
 
 
 
@
s
t
a
t
i
c
m
e
t
h
o
d


 
 
 
 
d
e
f
 
c
y
a
n
(
t
e
x
t
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
t
e
x
t
 
i
n
 
c
y
a
n
 
c
o
l
o
r
"
"
"


import unittest

class TestColors(unittest.TestCase):

    def test_red(self):
        """Test the red color method"""
        input_text = "Hello"
        expected_output = "\033[91mHello\033[0m"
        self.assertEqual(Colors.red(input_text), expected_output)

    def test_green(self):
        """Test the green color method"""
        input_text = "Hello"
        expected_output = "\033[92mHello\033[0m"
        self.assertEqual(Colors.green(input_text), expected_output)

    def test_blue(self):
        """Test the blue color method"""
        input_text = "Hello"
        expected_output = "\033[94mHello\033[0m"
        self.assertEqual(Colors.blue(input_text), expected_output)

    def test_yellow(self):
        """Test the yellow color method"""
        input_text = "Hello"
        expected_output = "\033[93mHello\033[0m"
        self.assertEqual(Colors.yellow(input_text), expected_output)

    def test_magenta(self):
        """Test the magenta color method"""
        input_text = "Hello"
        expected_output = "\033[95mHello\033[0m"
        self.assertEqual(Colors.magenta(input_text), expected_output)

    def test_cyan(self):
        """Test the cyan color method"""
        input_text = "Hello"
        expected_output = "\033[96mHello\033[0m"
        self.assertEqual(Colors.cyan(input_text), expected_output)

    def test_combined_colors(self):
        """Test combining different color methods"""
        input_text_red = Colors.red("Red")
        input_text_blue = Colors.blue("Blue")
        input_text_combined = f"{input_text_red} and {input_text_blue}"
        expected_output = "\033[91mRed\033[0m and \033[94mBlue\033[0m"
        self.assertEqual(input_text_combined, expected_output)

if __name__ == '__main__':
    unittest.main()