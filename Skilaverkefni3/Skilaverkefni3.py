#Skil3
'''

'''
import os
import sys

def get_filename():
    file_name = input("Enter filename: ")
    file_path = os.path.join(os.path.dirname(__file__),file_name)
    word_list = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for word in file:
                word = word[:-1]
                word_list.append(word)
        return word_list
    else:
        print ("File not found!")
        sys.exit(5)

def actions(word_list):
    answer = input("Enter action: ")
    while answer != "q":
        if answer[0:2] == "l/":
            line_number(word_list)
        elif answer[0:2] == "s/":
            search_string(word_list)
        elif answer[0:2] == "a/":
            append_word(word_list)
        elif answer == "w":
            write_list(word_list)

def line_number(word_list):



def main():
    word_list = get_filename()
    print (word_list)
    actions(word_list)

main()