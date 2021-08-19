#!/usr/bin/env python3
import re

WORD_HASH = {
    "small": "smol",
    "cute": "kawaii~",
    "fluff": "floof",
    "love": "luv",
    "stupid": "baka",
    "idiot": "baka",
    "what": "nani",
    "meow": "nya~",
    "roar": "rawrr~",
}

uwugex = re.compile(r"(?<![wrl])[lr](?![wrl])") # Laundmo certified UwUgex

def word_replace(input_string: str) -> str:
    for word in WORD_HASH: # Python sucks because Verboof doesn't let me do what I want :c
        input_string = input_string.replace(word, WORD_HASH[word])

    return input_string

def char_replace(input_string: str) -> str:
    return uwugex.sub("w", input_string)

