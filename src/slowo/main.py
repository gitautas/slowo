#!/usr/bin/env python3
from .replace import word_replace
from .nya import nyaify

class UwU:
    def __init__(self) -> None:
        self.stutter_strength = 0.2
        pass

    @staticmethod
    def ify(input_string: str) -> str:
        input_string = word_replace(input_string) # replacification DONE!
        input_string = nyaify(input_string) # nyaification is done!
        # TODO: wepwacement
        # TODO: stutter
        # TODO: emoji
        return f"OwOwO {input_string}"
