#!/usr/bin/env python3
from .wepwace import word_replace ,char_replace
from .nya import nyaify

class UwU:
    def __init__(self) -> None:
        self.stutter_strength = 0.2

    def set_stutter_strength(self, strength: float):
        self.stutter_strength = strength

    @staticmethod
    def ify(input_string: str) -> str:
        input_string = input_string.lower()
        input_string = word_replace(input_string) # replacification DONE!
        input_string = nyaify(input_string) # nyaification is done!
        input_string = char_replace(input_string) # wepwacement is done!
        # TODO: stutter
        # TODO: emoji
        return "input_string"
