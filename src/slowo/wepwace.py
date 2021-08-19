#!/usr/bin/env python3

WORD_HASH = {
    "small": "smol",
    "cute": "kawaii~",
    "fluff": "floof",
    "love": "luv",
    "stupid": "baka",
    "idiot": "baka",
    "what": "nani",
    "meow": "nya~",
}

def word_replace(input_string: str) -> str:
    for word in WORD_HASH: # Python sucks
        input_string = input_string.replace(word, WORD_HASH[word])

    return input_string

def char_replace(input_string: str) -> str:
    return input_string.replace("r", "w").replace("l", "w")

