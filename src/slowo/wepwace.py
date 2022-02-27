#!/usr/bin/env python3
import re

WORDS = {
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

uwugex = re.compile(r"(?<!w)[lr](?!w)")  # Updated UwUgex


def word_replace(input_string: str) -> str:
    for word, changed_word in WORDS.items():
        input_string = input_string.replace(word, changed_word)

    return input_string


def char_replace(input_string: str) -> str:
    return uwugex.sub("w", input_string)
