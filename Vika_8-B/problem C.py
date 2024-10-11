#Engineering English

import sys

word_set = set()

for line in sys.stdin:
    words = line.split()
    for word in words:
        word_comparison = word.lower()
        if word_comparison in word_set:
            print (".", end=" ")
        else:
            word_set.add(word_comparison)
            print (word, end =" ")
    print ("\n")
    