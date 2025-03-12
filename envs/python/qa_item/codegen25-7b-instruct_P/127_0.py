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
 
s
e
p
a
r
a
t
e
_
o
c
t
a
v
e
_
a
n
d
_
r
o
o
t
(
m
i
d
i
_
n
o
t
e
s
:
 
L
i
s
t
[
i
n
t
]
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


 
 
 
 
S
p
l
i
t
s
 
a
 
l
i
s
t
 
o
f
 
M
I
D
I
 
n
o
t
e
 
n
u
m
b
e
r
s
 
i
n
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
 
l
i
s
t
s
 
o
f
 
o
c
t
a
v
e
s
 
a
n
d
 
r
o
o
t
 
n
o
t
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
i
d
i
_
n
o
t
e
s
 
(
L
i
s
t
[
i
n
t
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
 
M
I
D
I
 
n
o
t
e
 
n
u
m
b
e
r
s
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
 
l
i
s
t
s
 
o
f
 
o
c
t
a
v
e
s
 
a
n
d
 
r
o
o
t
 
n
o
t
e
s
.


 
 
 
 
"
"
"


 
 
 
 
o
c
t
a
v
e
s
 
=
 
[
]


 
 
 
 
r
o
o
t
s
 
=
 
[
]


 
 
 
 
f
o
r
 
n
o
t
e
 
i
n
 
m
i
d
i
_
n
o
t
e
s
:


 
 
 
 
 
 
 
 
o
c
t
a
v
e
 
=
 
n
o
t
e
 
/
/
 
1
2


 
 
 
 
 
 
 
 
r
o
o
t
 
=
 
n
o
t
e
 
%
 
1
2


 
 
 
 
 
 
 
 
o
c
t
a
v
e
s
.
a
p
p
e
n
d
(
o
c
t
a
v
e
)


 
 
 
 
 
 
 
 
r
o
o
t
s
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
o
t
)


 
 
 
 
r
e
t
u
r
n
 
{
"
o
c
t
a
v
e
s
"
:
 
o
c
t
a
v
e
s
,
 
"
r
o
o
t
s
"
:
 
r
o
o
t
s
}






d
e
f
 
g
e
t
_
m
i
d
i
_
n
o
t
e
_
n
a
m
e
s
(
m
i
d
i
_
n
o
t
e
s
:
 
L
i
s
t
[
i
n
t
]
)
-
>
L
i
s
t
[
s
t
r
]
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
 
l
i
s
t
 
o
f
 
M
I
D
I
 
n
o
t
e
 
n
u
m
b
e
r
s
 
t
o
 
a
 
l
i
s
t
 
o
f
 
n
o
t
e
 
n
a
m
e
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
i
d
i
_
n
o
t
e
s
 
(
L
i
s
t
[
i
n
t
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
 
M
I
D
I
 
n
o
t
e
 
n
u
m
b
e
r
s
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
s
t
r
]
:
 
A
 
l
i
s
t
 
o
f
 
n
o
t
e
 
n
a
m
e
s
.


 
 
 
 
"
"
"


 
 
 
 
n
a
m
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
n
o
t
e
 
i
n
 
m
i
d
i
_
n
o
t
e
s
:


 
 
 
 
 
 
 
 
o
c
t
a
v
e
 
=
 
n
o
t
e
 
/
/
 
1
2


 
 
 
 
 
 
 
 
r
o
o
t
 
=
 
n
o
t
e
 
%
 
1
2


 
 
 
 
 
 
 
 
n
a
m
e
s
.
a
p
p
e
n
d
(
f
"
{
r
o
o
t
_
t
o
_
n
a
m
e
(
r
o
o
t
)
}
{
o
c
t
a
v
e
}
"
)


 
 
 
 
r
e
t
u
r
n
 
n
a
m
e
s






d
e
f
 
g
e
t
_
m
i
d
i
_
n
o
t
e
_
n
a
m
e
s
_
w
i
t
h
_
o
c
t
a
v
e
(
m
i
d
i
_
n
o
t
e
s
:
 
L
i
s
t
[
i
n
t
]
)
-
>
L
i
s
t
[
s
t
r
]
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
 
l
i
s
t
 
o
f
 
M
I
D
I
 
n
o
t
e
 
n
u
m
b
e
r
s
 
t
o
 
a
 
l
i
s
t
 
o
f
 
n
o
t
e
 
n
a
m
e
s
 
w
i
t
h
 
o
c
t
a
v
e
 
n
u
m
b
e
r
s
.




 
 
 
 
A
r
g
s
:


 
 
 
 
 
 
 
 
m
i
d
i
_
n
o
t
e
s
 
(
L
i
s
t
[
i
n
t
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
 
M
I
D
I
 
n
o
t
e
 
n
u
m
b
e
r
s
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
s
t
r
]
:
 
A
 
l
i
s
t
 
o
f
 
n
o
t
e
 
n
a
m
e
s
 
w
i
t
h
 
o
c
t
a
v
e
 
n
u
m
b
e
r
s
.


 
 
 
 
"
"
"


 
 
 
 
n
a
m
e
s
 
=
 
[
]


 
 
 
 
f
o
r
 
n
o
t
e
 
i
n
 
m
i
d
i
_
n
o
t
e
s
:


 
 
 
 
 
 
 
 
o
c
t
a
v
e
 
=
 
n
o
t
e
 
/
/
 
1
2


 
 
 
 
 
 
 
 
r
o
o
t
 
=
 
n
o
t
e
 
%
 
1
2


 
 
 
 
 
 
 
 
n
a
m
e
s
.
a
p
p
e
n
d
(
f
"
{
r
o
o
t
_
t
o
_
n
a
m
e
(
r
o
o
t
)
}
{
o
c
t
a
v
e
}
"
)


 
 
 
 
r
e
t
u
r
n
 
n
a
m
e
s






d
e
f
 
g
e
t
_
m
i
d
i
_
n
o
t
e
_
n
a
m
e
s
_
w
i
t
h
_
o
c
t
a
v
e
_
a
n
d
_
r
o
o
t
(
m
i
d
i
_
n
o
t
e
s
:
 
L
i
s
t
[
i
n
t
]
)
-
>
L
i
s
t
[
s
t
r
]
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
import unittest


class TestSeparateOctaveAndRoot(unittest.TestCase):

    def test_correctly_separates_midi_notes(self):
        midi_notes = [60, 61, 62]  # C4, C#4, D4
        expected = {
            'octaveNotes': [5, 5, 5],  # All notes are in the 5th octave
            'rootNotes': [0, 1, 2]     # Root notes are C, C#, D
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

    def test_handles_single_midi_note_input(self):
        midi_notes = [24]  # C1
        expected = {
            'octaveNotes': [2],  # 2nd octave
            'rootNotes': [0]     # C note
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

    def test_returns_empty_arrays_for_empty_input_array(self):
        midi_notes = []
        expected = {
            'octaveNotes': [],
            'rootNotes': []
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

    def test_throws_error_for_invalid_input_types(self):
        invalid_inputs = ["not an array", [3.14]]
        for invalid_input in invalid_inputs:
            with self.assertRaises(TypeError):
                separate_octave_and_root(invalid_input)

    def test_handles_midi_notes_from_different_octaves(self):
        midi_notes = [12, 25, 37]  # C1, C#2, D#3
        expected = {
            'octaveNotes': [1, 2, 3],  # 1st, 2nd, and 3rd octaves
            'rootNotes': [0, 1, 1]     # Root notes are C, C#, D#
        }
        self.assertEqual(separate_octave_and_root(midi_notes), expected)

if __name__ == '__main__':
    unittest.main()