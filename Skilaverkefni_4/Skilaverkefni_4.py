#Elections
import os

def show_menu(constituencies_dict, parties_dict, result_dict):
    '''
    Displays a menu to choose actions in, sends dicts between various functions that it gets from main function 
     and sends back between new actions 
    has a boolean return for quitting the program, 
    '''

    choice = None

    while choice not in ["1", "2", "3", "9"]:
        print ()        
        print ("1. Show constituencies")
        print ("2. Show parties")
        print ("3. Show results")
        print ("9. Quit")
        print ()
        choice = input ("Select an action: ")

        if choice == "1": 
            constituencies_dict = show_constituencies(constituencies_dict)
        elif choice == "2":
            parties_dict = show_parties(parties_dict)
        elif choice == "3":
            result_dict = show_results(constituencies_dict, parties_dict, result_dict)
        elif choice == "9":
            return constituencies_dict, parties_dict, result_dict, False
        
        return constituencies_dict, parties_dict, result_dict, True

def get_file(file_type = ""):
    '''
    this function is  for loading  files into dictionaries, it has slightly different logic for result files. 
    it then returns the dictionary ready for use in the program. If dict is not found then it returns an emtpy dict,
    prompting the main menu again. 
    '''

    temp_dict = {}

    if file_type == "results":
        file_name = input("File name for results: ")
    else:
        file_name = input("File name: ")
    file_path = os.path.join(os.path.dirname(__file__),file_name)

    try:
        with open(file_path, "r") as file:
            if file_type == "results":
                results = {}
                for line in file:
                    line = line.strip()
                    if ";" not in line:
                        current_constituency = line
                        results[current_constituency] = [] 
                    else:
                            party, votes = line.split(";")
                            votes = int(votes)
                            results[current_constituency].append((party, votes))
                return results 
            
            else:
                for line in file:
                    line = line.strip().split(";")
                    temp_dict[line[0]] = line[1]

    except FileNotFoundError:
        return {}
    return temp_dict

def show_constituencies(constituencies_dict):
    '''
    checks if there is dict already, if not then gets one via get file function. 
    Prints out the text as requested by assignment.
    '''

    if len(constituencies_dict) == 0:
        constituencies_dict = get_file()
        if len(constituencies_dict) == 0:
            return constituencies_dict
    electoral_sum = sum(int(electorals) for electorals in constituencies_dict.values())

    print ()
    print(f"{'Constituency' :<19} {'Electorals' :>8}")
    print ("-" * 30)
    for const, electorals in constituencies_dict.items():
        print (f"{const :<20} {electorals :>{9}}")
    print ("-" * 30)
    print(f"{'Total:' :<20} {electoral_sum :>{9}}")
    return constituencies_dict


def show_parties(parties_dict):
    '''
    checks if there is a dict, if not then gets one via get_file. If it returns an empty one then returns to main menu
    otherwise prints out everything as requested by assignment. 
    '''

    if len(parties_dict) == 0:
        parties_dict = get_file()
    if len(parties_dict) == 0:
        return parties_dict
    
    print ()
    print(f"{'List' :<5} {'Party' :>{26}}")
    print("-" * 32)
    for list_char, party_name in parties_dict.items():
        print(f"{list_char :<5} {party_name :>{26}}")

    return parties_dict

def show_results(constituencies_dict, parties_dict, result_dict):
    '''
    checks if const and parties have been loaded, if not then throws a dummy input to get past kattiss and returns. 
    otherwise it gets file and asks for const name to show results for that constituency
    prints the text as requested 
    '''

    if len(constituencies_dict) == 0 or len(parties_dict) == 0:
        input("File name for results: ")
        return result_dict
    
    if len(result_dict) == 0:  
        result_dict = get_file("results")
        if len(result_dict) == 0:
            return result_dict
        
    constituency_name = input("Constituency: ")
    if constituency_name not in result_dict:
        return result_dict
    
    constituency_results = result_dict[constituency_name]
    total_votes = sum(votes for _, votes in constituency_results)
    electoral_count = int(constituencies_dict[constituency_name])
    turnout_ratio = total_votes / electoral_count if electoral_count > 0 else 0

    print ()
    print (constituency_name)
    print(f"{'List' :<10} {'Party' :>25} {'Votes' :>9} {'Ratio' :>9}")
    print("-" * 56)

    for party_letter, votes in constituency_results:
        party_name = parties_dict.get(party_letter, "Unknown")
        ratio = (votes / total_votes * 100) if total_votes > 0 else 0
        print(f"{party_letter :<10} {party_name :>25} {votes :>9} {ratio :>9.1f}")

    print("-" * 56)
    print(f"{'Total:' :<10} {total_votes :>35} {100.0 :>9.1f}")
    print(f"{'Turnout:' :<10} {turnout_ratio * 100 :>45.1f}")
    
    return result_dict
    
def main():
    '''
    initalizes all the dicts used in the program, also a flag to flag in case the program should shut off. 
    Then triggers show_menu until flag gets returned as False. 
    '''

    constituencies_dict = {}  
    parties_dict = {}
    result_dict = {}
    on_flag = True

    while on_flag:
        constituencies_dict, parties_dict, result_dict, on_flag = show_menu(constituencies_dict, parties_dict, result_dict)


main()




