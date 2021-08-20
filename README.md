<!-- ABOUT -->
## About 

An uwuifier written in python, based on the uwugorithms from Danny Liuwu's [uwuifier.](https://github.com/Daniel-Liu-c0deb0t/uwu)

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

All you need to install slowo is any relatively recent version of Python3

### Installation

   ```sh
   python3 -m pip install slowo
   ```

<!-- USAGE EXAMPLES -->
## Usage

Currently I haven't made an executable to run the uwuizer from your shell easily, but you can easily make one like this:

```py
#!/usr/bin/env python3
import slowo
import sys

print(slowo.UwU.ify(sys.argv[1]))
```

to pass your string as a shell arg or 

```py
#!/usr/bin/env python3
import slowo

print(slowo.UwU.ify(input()))
```

to uwuify from STDIN.

otherwise using the static method `slowo.UwU.ify()` you can uwuify your strings in your code.

Additionally, there are two optional arguments to this method called `stutter_strength` and `emoji_strength` where you can pass a float value from 0 to 1 to signify the weight of emojis and stuttering.
