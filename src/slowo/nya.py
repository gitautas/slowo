#!/usr/bin/env python3
import re

uwugex = re.compile(r"n([aeou])([^aeiou])")# TODO: look into regex
substitute = "ny\\g<1>\\g<2>"

def nyaify(input_string):
    return uwugex.sub(substitute, input_string, 0)
