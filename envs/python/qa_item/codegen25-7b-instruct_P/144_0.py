d
e
f
 
a
r
a
b
i
c
_
t
o
_
e
n
g
l
i
s
h
_
n
u
m
b
e
r
s
(
v
a
l
u
e
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


 
 
 
 
C
o
n
v
e
r
t
s
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
i
n
 
a
 
s
t
r
i
n
g
 
t
o
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
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
 
i
t
e
r
a
t
e
s
 
o
v
e
r
 
e
a
c
h
 
c
h
a
r
a
c
t
e
r
 
i
n
 
t
h
e
 
i
n
p
u
t
 
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
i
n
g
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
(
٠
-
٩
)


 
 
 
 
w
i
t
h
 
t
h
e
i
r
 
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
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
l
s
 
(
0
-
9
)
 
w
h
i
l
e
 
l
e
a
v
i
n
g
 
o
t
h
e
r
 
c
h
a
r
a
c
t
e
r
s
 
u
n
c
h
a
n
g
e
d
.


 
 
 
 
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
 
٠
١
٢
٣
٤
٥
٦
٧
٨
٩


 
 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
0
1
2
3
4
5
6
7
8




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
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
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
t
o
 
b
e
 
c
o
n
v
e
r
t
e
d
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
v
e
r
t
e
d
 
s
t
r
i
n
g
 
w
i
t
h
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
r
e
p
l
a
c
e
d
 
b
y
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
l
s
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
r
e
.
s
u
b
(
r
'
[
٠
١
٢
٣
٤
٥
٦
٧
٨
٩
]
'
,
 
l
a
m
b
d
a
 
x
:
 
s
t
r
(
i
n
t
(
x
.
g
r
o
u
p
(
0
)
)
)
,
 
v
a
l
u
e
)






d
e
f
 
e
n
g
l
i
s
h
_
t
o
_
a
r
a
b
i
c
_
n
u
m
b
e
r
s
(
v
a
l
u
e
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


 
 
 
 
C
o
n
v
e
r
t
s
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
l
s
 
i
n
 
a
 
s
t
r
i
n
g
 
t
o
 
A
r
a
b
i
c
 
n
u
m
e
r
a
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
 
i
t
e
r
a
t
e
s
 
o
v
e
r
 
e
a
c
h
 
c
h
a
r
a
c
t
e
r
 
i
n
 
t
h
e
 
i
n
p
u
t
 
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
i
n
g
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
l
s
 
(
0
-
9
)


 
 
 
 
w
i
t
h
 
t
h
e
i
r
 
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
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
(
٠
-
٩
)
 
w
h
i
l
e
 
l
e
a
v
i
n
g
 
o
t
h
e
r
 
c
h
a
r
a
c
t
e
r
s
 
u
n
c
h
a
n
g
e
d
.


 
 
 
 
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
 
0
1
2
3
4
5
6
7
8


 
 
 
 
 
 
 
 
 
o
u
t
p
u
t
:
 
٠
١
٢
٣
٤
٥
٦
٧
٨
٩




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
v
a
l
u
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
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
l
s
 
t
o
 
b
e
 
c
o
n
v
e
r
t
e
d
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
v
e
r
t
e
d
 
s
t
r
i
n
g
 
w
i
t
h
 
E
n
g
l
i
s
h
 
n
u
m
e
r
a
l
s
 
r
e
p
l
a
c
e
d
 
b
y
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
.


 
 
 
 
"
"
"


 
 
 
 
r
e
t
u
r
n
 
r
e
.
s
u
b
(
r
'
[
0
-
9
]
'
,
 
l
a
m
b
d
a
 
x
:
 
s
t
r
(
i
n
t
(
x
.
g
r
o
u
p
(
0
)
)
 
+
 
4
8
)
,
 
v
a
l
u
e
)






d
e
f
 
a
r
a
b
i
c
_
t
o
_
p
e
r
s
i
a
n
_
n
u
m
b
e
r
s
(
v
a
l
u
e
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


 
 
 
 
C
o
n
v
e
r
t
s
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
i
n
 
a
 
s
t
r
i
n
g
 
t
o
 
P
e
r
s
i
a
n
 
n
u
m
e
r
a
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
 
i
t
e
r
a
t
e
s
 
o
v
e
r
 
e
a
c
h
 
c
h
a
r
a
c
t
e
r
 
i
n
 
t
h
e
 
i
n
p
u
t
 
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
i
n
g
 
A
r
a
b
i
c
 
n
u
m
e
r
a
l
s
 
(
٠
-
٩
)


 
 
 
 
w
i
t
h
 
t
h
e
i
r
 
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
 
P
e
r
s
i
a
n
 
n
u
m
e
r
a
l
s
 
(
۰
-
۹
)
 
w
h
i
l
e
 
l
e
a
v
i
n
g
 
o
t
h
e
r
 
c
h
a
r
a
c
t
e
r
s
 
u
n
c
h
a
n
g
e
d
.


 
 
 
 
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
 
٠
١
٢
٣
import unittest

class TestArabicToEnglishNumbers(unittest.TestCase):
    
    def test_converts_single_arabic_numerals_to_english(self):
        self.assertEqual(arabic_to_english_numbers('١'), '1')
        self.assertEqual(arabic_to_english_numbers('٥'), '5')
        self.assertEqual(arabic_to_english_numbers('٩'), '9')

    def test_converts_a_string_of_arabic_numerals_to_english(self):
        self.assertEqual(arabic_to_english_numbers('٠١٢٣٤٥٦٧٨٩'), '0123456789')

    def test_handles_strings_with_arabic_and_english_numerals_mixed(self):
        self.assertEqual(arabic_to_english_numbers('٠١23٤5'), '012345')

    def test_leaves_non_numeral_characters_unchanged(self):
        self.assertEqual(arabic_to_english_numbers('Hello World!'), 'Hello World!')
        self.assertEqual(arabic_to_english_numbers('2022-٢٠٢٣'), '2022-2023')

    def test_works_with_full_sentences_that_include_arabic_numerals(self):
        self.assertEqual(arabic_to_english_numbers('The year is ٢٠٢٤!'), 'The year is 2024!')

    def test_handles_empty_strings_correctly(self):
        self.assertEqual(arabic_to_english_numbers(''), '')

    def test_processes_arabic_numerals_in_a_complex_mixed_context(self):
        self.assertEqual(arabic_to_english_numbers('Price: ٥٠٠$ and Date: ٢٠٢٣-١٢-٠١'), 'Price: 500$ and Date: 2023-12-01')

if __name__ == '__main__':
    unittest.main()