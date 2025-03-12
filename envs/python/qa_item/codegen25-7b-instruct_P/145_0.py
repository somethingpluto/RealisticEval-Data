d
e
f
 
f
o
r
m
a
t
_
c
u
r
r
e
n
c
y
(
v
a
l
u
e
:
 
f
l
o
a
t
,
 
c
u
r
r
e
n
c
y
_
c
o
d
e
:
 
s
t
r
,
 
l
o
c
a
l
e
:
 
s
t
r
 
=
 
"
e
n
_
U
S
"
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
o
r
m
a
t
s
 
a
 
n
u
m
b
e
r
 
a
s
 
c
u
r
r
e
n
c
y
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
l
o
c
a
l
e
 
a
n
d
 
c
u
r
r
e
n
c
y
 
c
o
d
e
.




 
 
 
 
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
f
l
o
a
t
)
:
 
T
h
e
 
n
u
m
e
r
i
c
a
l
 
v
a
l
u
e
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
.


 
 
 
 
 
 
 
 
c
u
r
r
e
n
c
y
_
c
o
d
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
 
c
u
r
r
e
n
c
y
 
c
o
d
e
 
(
e
.
g
.
,
 
"
U
S
D
"
,
 
"
E
U
R
"
)
.


 
 
 
 
 
 
 
 
l
o
c
a
l
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
 
l
o
c
a
l
e
 
s
t
r
i
n
g
 
(
e
.
g
.
,
 
"
e
n
_
U
S
"
,
 
"
f
r
_
F
R
"
)
.
 
D
e
f
a
u
l
t
 
i
s
 
"
e
n
_
U
S
"
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
 
f
o
r
m
a
t
t
e
d
 
c
u
r
r
e
n
c
y
 
s
t
r
i
n
g
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
 
f
"
{
c
u
r
r
e
n
c
y
_
c
o
d
e
}
 
{
f
o
r
m
a
t
_
n
u
m
b
e
r
(
v
a
l
u
e
,
 
l
o
c
a
l
e
=
l
o
c
a
l
e
)
}
"






d
e
f
 
f
o
r
m
a
t
_
p
e
r
c
e
n
t
a
g
e
(
v
a
l
u
e
:
 
f
l
o
a
t
,
 
l
o
c
a
l
e
:
 
s
t
r
 
=
 
"
e
n
_
U
S
"
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
o
r
m
a
t
s
 
a
 
n
u
m
b
e
r
 
a
s
 
p
e
r
c
e
n
t
a
g
e
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
l
o
c
a
l
e
.




 
 
 
 
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
f
l
o
a
t
)
:
 
T
h
e
 
n
u
m
e
r
i
c
a
l
 
v
a
l
u
e
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
.


 
 
 
 
 
 
 
 
l
o
c
a
l
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
 
l
o
c
a
l
e
 
s
t
r
i
n
g
 
(
e
.
g
.
,
 
"
e
n
_
U
S
"
,
 
"
f
r
_
F
R
"
)
.
 
D
e
f
a
u
l
t
 
i
s
 
"
e
n
_
U
S
"
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
 
f
o
r
m
a
t
t
e
d
 
p
e
r
c
e
n
t
a
g
e
 
s
t
r
i
n
g
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
 
f
"
{
v
a
l
u
e
:
.
2
%
}
"






d
e
f
 
f
o
r
m
a
t
_
p
e
r
c
e
n
t
a
g
e
_
w
i
t
h
_
m
u
l
t
i
p
l
i
e
r
(


 
 
 
 
v
a
l
u
e
:
 
f
l
o
a
t
,
 
m
u
l
t
i
p
l
i
e
r
:
 
i
n
t
,
 
l
o
c
a
l
e
:
 
s
t
r
 
=
 
"
e
n
_
U
S
"


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
o
r
m
a
t
s
 
a
 
n
u
m
b
e
r
 
a
s
 
p
e
r
c
e
n
t
a
g
e
 
w
i
t
h
 
m
u
l
t
i
p
l
i
e
r
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
l
o
c
a
l
e
.




 
 
 
 
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
f
l
o
a
t
)
:
 
T
h
e
 
n
u
m
e
r
i
c
a
l
 
v
a
l
u
e
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
.


 
 
 
 
 
 
 
 
m
u
l
t
i
p
l
i
e
r
 
(
i
n
t
)
:
 
T
h
e
 
m
u
l
t
i
p
l
i
e
r
 
t
o
 
b
e
 
u
s
e
d
.


 
 
 
 
 
 
 
 
l
o
c
a
l
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
 
l
o
c
a
l
e
 
s
t
r
i
n
g
 
(
e
.
g
.
,
 
"
e
n
_
U
S
"
,
 
"
f
r
_
F
R
"
)
.
 
D
e
f
a
u
l
t
 
i
s
 
"
e
n
_
U
S
"
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
 
f
o
r
m
a
t
t
e
d
 
p
e
r
c
e
n
t
a
g
e
 
s
t
r
i
n
g
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
 
f
"
{
v
a
l
u
e
:
.
2
%
}
 
(
{
m
u
l
t
i
p
l
i
e
r
}
x
)
"






d
e
f
 
f
o
r
m
a
t
_
p
e
r
c
e
n
t
a
g
e
_
w
i
t
h
_
m
u
l
t
i
p
l
i
e
r
_
a
n
d
_
u
n
i
t
(


 
 
 
 
v
a
l
u
e
:
 
f
l
o
a
t
,
 
m
u
l
t
i
p
l
i
e
r
:
 
i
n
t
,
 
u
n
i
t
:
 
s
t
r
,
 
l
o
c
a
l
e
:
 
s
t
r
 
=
 
"
e
n
_
U
S
"


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
o
r
m
a
t
s
 
a
 
n
u
m
b
e
r
 
a
s
 
p
e
r
c
e
n
t
a
g
e
 
w
i
t
h
 
m
u
l
t
i
p
l
i
e
r
 
a
n
d
 
u
n
i
t
 
a
c
c
o
r
d
i
n
g
 
t
o
 
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
 
l
o
c
a
l
e
.




 
 
 
 
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
f
l
o
a
t
)
:
 
T
h
e
 
n
u
m
e
r
i
c
a
l
 
v
a
l
u
e
 
t
o
 
b
e
 
f
o
r
m
a
t
t
e
d
.


import unittest

class TestFormatCurrency(unittest.TestCase):
    
    def test_format_currency_usd(self):
        value = 1234.56
        currency_code = 'USD'
        locale = 'en-US'
        expected_output = '\$1,234.56'  # Expected format for USD
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_euro(self):
        value = 1234.56
        currency_code = 'EUR'
        locale = 'en-US'
        expected_output = '€1,234.56'  # Expected format for EUR
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_gbp(self):
        value = 1234.56
        currency_code = 'GBP'
        locale = 'en-GB'
        expected_output = '£1,234.56'  # Expected format for GBP
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_negative(self):
        value = -1234.56
        currency_code = 'USD'
        locale = 'en-US'
        expected_output = '-\$1,234.56'  # Expected format for negative USD
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)

    def test_format_currency_zero(self):
        value = 0
        currency_code = 'JPY'
        locale = 'en-JP'
        expected_output = '¥0'  # Expected format for JPY (no decimals)
        self.assertEqual(format_currency(value, currency_code, locale), expected_output)
if __name__ == '__main__':
    unittest.main()