#!/usr/bin/env python

# Run with `python -m pdb <script.py>` or `python3 -m pdb <script.py>`

# Do the basics in pdb:
# Get built-in help (help and ?)
# Show current context (list or list 16, 19 or longlist in python3)
# Run script until next breakpoint (continue)
# Repeat last command (press return)
# Write some python code: for i in range 10: print(i)
# Print a value (print i or pp for pretty printing)
# Set break point (break), c(continue) and remove them (clear) again
# Show brekpoint(s) (break)

a = 23
b = 42

# Swap using a helper variable:
tmp = a
a = b
b = tmp

# Swapping more pythonic:
a, b = b, a
