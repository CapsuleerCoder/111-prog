#Interleave Two Files


import os
file_input1 = input()
file_input2 = input()
filename1 = os.path.join(os.path.dirname(__file__), file_input1)
filename2 = os.path.join(os.path.dirname(__file__), file_input2)

with open (filename1, "r") as file1, open (filename2, "r") as file2:
