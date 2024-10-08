# Reverse Words

import os
file_input = input()
filename = os.path.join(os.path.dirname(__file__), file_input)

with open (filename, "r") as file:
    for line in file:
        words_in_line = line.split()
        reversed = []
        for word in words_in_line:
            reversed.append(word[::-1])
        print (" ".join(reversed))
