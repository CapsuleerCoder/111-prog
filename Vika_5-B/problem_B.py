# Countries

import os

def find_countries(ending):
        filename = os.path.join(os.path.dirname(__file__),"countries.txt")
        teljari = 0
        with open (filename, "r") as file:
            for line in file: 
                line = line.strip()
                if line.endswith(ending):
                     print(line)
                     teljari += 1
        print (f"{teljari} countries with suffix {ending} in total.")
