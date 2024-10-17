#Elections
import os
import sys

def show_menu():
    print ("1. Show constituencies")
    print ("2. Show parties")
    print ("3. Show results")
    print ("4. Quit")

def get_file():
    temp_dict = {}
    file_name = input("File name: ")
    file_path = os.path.join(os.path.dirname(__file__),file_name)
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip().split(";")
            temp_dict.update({line[0]: line[1]})
    return temp_dict

def show_constituencies(constituencies_dict):
    if len(constituencies_dict) == 0:
        constituencies_dict = get_file()
        ELECTORAL_SUM = sum(int(electorals) for electorals in constituencies_dict.values())
    print (f"{"Constituency" :<{20}} {"Electorals" :>{10}}")
    print ("-"*31)
    for const, electorals in constituencies_dict.items():
        print (f"{const :<{20}} {electorals :>{10}}")
    print ("-"*31)
    print (f"{"Total:":<{20}} {ELECTORAL_SUM :>{10}}")

#def show_parties():

#def show_results():

def choose_action():


def main():
    show_constituencies()

main()




