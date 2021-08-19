#!/usr/bin/env python3
import random
import re
from functools import partial

uwugex = re.compile(r"(\s)([a-zA-Z])")
subst = "\\g<1>\\g<2>-\\g<2>"

def stutter(strength: float, input_string: str):
        return uwugex.sub(partial(replace, strength=strength), input_string, 0)

def replace(match, strength = 0.0):
    match_string = match.string[slice(*match.span())]
    if random.random() < strength:
        char = match_string[-1]
        return f"{match_string}-{char}"
    return match_string