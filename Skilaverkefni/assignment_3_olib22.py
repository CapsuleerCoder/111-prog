# Word List - olib22
import os
import sys

def get_list():
    '''
    Return a list of words from a file or (none, none) if not found 
    '''
    file_name = input("Enter filename: ")
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    word_list =  []
    if os.path.exists(file_path):
        with open (file_path, "r") as file:
            for word_in_line in file:
                word_in_line = word_in_line.strip()
                word_list.append(word_in_line)
        return word_list, file_path
    else:
        print ("File not found!")
        return None, None

def actions(word_list, file_path):
    '''
    Prompts user for action which calls various functions until q is entered
    '''
    answer = ""
    while answer != "q":
            answer = input("Enter action: ")
            if len(answer) > 2:
                if answer[:2] == "l/":
                    line_number(answer, word_list)
                elif answer[:2] == "s/":
                    search_str(answer, word_list)
                elif answer[:2] == "a/":
                    append_word(answer, word_list)
            else:
                if answer == "w":
                    write_to_file(word_list, file_path)

def line_number(answer, line_number):
    '''
    Extracts the line number after the command from answer, prints out that line in the list with a -1 to account for python index
    '''
    try:
        answer = (int(answer[2:])-1)
        print (line_number[answer])
    except (IndexError, ValueError):
        print ("Invalid line number")

def search_str(answer, word_list):
    '''
    Loops through the words searching for similarities and prints the word if so. 
    '''
    answer = answer[2:]
    for word in word_list:
        if answer in word:
            print (word)

def append_word(answer, word_list):
    '''
    Appends word to the list being referenced by all functions
    '''
    word_list.append(answer[2:])

def write_to_file(word_list,file_path):
    '''
    Writes the word list back to file, overwrites the old and flushes it after. 
    '''
    with open (file_path, "w") as file:
        file.seek(0)
        for word in word_list:
            file.write(word + "\n")
        file.flush()
    print("File written!")

def main():
    '''
    We call get_list() to get word list for all functions, and file path for use in write_to_file()
    We quit the program if file was not found, otherwise we call action() and start the loop. 
    '''
    word_list, file_path = get_list()
    if word_list is None:
        return
    actions(word_list, file_path)

main()