## Copyright (C) 2024, Nicholas Carlini <nicholas@carlini.com>.
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.


# This file is terrible code.
# In my defense it's mostly written by GPT-4.
# I am very sorry.
# At some point I might clean it up.

import markdown
import ast
from PIL import Image
import numpy as np
import io
import re

import pygments.lexers
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from evaluator import *

def fix(x):
    return "\n".join("> "+line for line in x.split("\n"))

def format_markdown(reason, indent=0):
        return "UNKNOWN NODE TYPE: " + repr(reason.node)


def generate_report(data, tags, descriptions):
            open("evaluation_examples/"+column_key+"_"+row_key+".html", "w").write(css+example_html)

def convert_to_color_through_yellow(value):
    value *= 255

    # Determine the stage of interpolation
    if value <= 127.5:
        # Stage 1: Red to Yellow
        red = 255
        green = int(value) + 127.5  # Green increases from 0 to 255
        blue = 127.5
    else:
        # Stage 2: Yellow to Green
        red = int(255 - (value - 127.5))  # Red decreases from 255 to 0
        green = 255
        blue = 127.5

    return red, green, blue            