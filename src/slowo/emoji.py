#!/usr/bin/env python3
import random
import re
from functools import partial

EMOJI_LUT = [
    "rawr x3",
    "OwO",
    "UwU",
    "o.O",
    "-.-",
    ">w<",
    "(⑅˘꒳˘)",
    "(ꈍᴗꈍ)",
    "(˘ω˘)",
    "(U ᵕ U❁)",
    "σωσ",
    "òωó",
    "(///ˬ///✿)",
    "(U ﹏ U)",
    "( ͡o ω ͡o )",
    "ʘwʘ",
    ":3",
    ":3", # important enough to have twie
    "XD",
    "nyaa~~",
    "mya",
    ">_<",
    "😳",
    "🥺",
    "😳😳😳",
    "rawr",
    "^^",
    "^^;;",
    "(ˆ ﻌ ˆ)♡",
    "^•ﻌ•^",
    "/(^•ω•^)",
    "(✿oωo)",
]

punctuation_regex = re.compile(r"[\.!\?;\s]+")

def emoji(strength: float, input_string: str):
        return punctuation_regex.sub(partial(replace, strength=strength), input_string, 0)


def replace(match, strength = 0.0):
    match_string = match.string[slice(*match.span())]
    if random.random() < strength:
        return f"{match_string} " + EMOJI_LUT[random.randint(0, len(EMOJI_LUT) - 1)] + " "

    return match_string