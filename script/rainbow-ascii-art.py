#!/bin/env python

import random
import pyfiglet

text = "hi,hxf" 

font = "slant"

color_code = {'red': '\033[31m',
              'green': '\033[32m',
              'yellow': '\033[33m',
              'blue': '\033[34m',
              'violet': '\033[35m',
              'azure': '\033[36m'
              }

color = random.choice(list(color_code.keys()))

string = color_code[color] + pyfiglet.figlet_format(text, font) + '\033[0m'

print("\n" + string)
