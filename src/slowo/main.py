#!/usr/bin/env python3
from .wepwace import word_replace ,char_replace
from .nya import nyaify
from .stutter import stutter

class UwU:
    @staticmethod
    def ify(input_string: str, stutter_strength: float = 0.1) -> str:
        input_string = input_string.lower()
        input_string = word_replace(input_string) # replacification DONE!
        input_string = nyaify(input_string) # nyaification is done!
        input_string = char_replace(input_string) # wepwacement is done!
        input_string = stutter(stutter_strength, input_string) # after lots of toil, stuttering is d-done...
        # TODO: emoji
        print(input_string)
        return "input_string"
