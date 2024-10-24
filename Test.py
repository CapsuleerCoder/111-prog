

# def get_input_list(input_count):
#     if input_count < 1:
#         return None
#     else:
#         input_list = []
#         for count in range(input_count):
#             input_number = int(input("Enter a number to add to list: "))
#             input_list.append(input_number)
#         return input_list

# def average_of_list(list_to_avg):
#     sum_of_list = 0
#     for number in list_to_avg:
#         sum_of_list += number
#     avg_list = sum_of_list/(len(list_to_avg))
#     return avg_list

# def triple_values(input_list):
#     for index in range(len(input_list)):
#         input_list[index] *= 3

# number_of_inputs = int(input("How many numbers will you input? "))
# input_list = get_input_list(number_of_inputs)
# if input_list == None:
#     print ("Not valid")
# else:
#     print (f"The list: {input_list}")
#     average = average_of_list(input_list)
#     print (f"The average of the values is {average}")
#     triple_values(input_list)
#     print (f"Now the list: {input_list}")

# def make_dict(number):
#     name_dict = {}
#     for _ in range(number):
#         user_id = int(input("What is the id? "))
#         user_name = input("What is the name?")
#         name_dict.update({user_id : user_name})
#     return name_dict

# def id_lookup(name_dict):
#     answer = ""
#     while answer != "q":
#         answer = input("What id to look up? ")
#         if answer == "q": 
#             print ("Quitting")
#             return
#         else:
#             answer = int(answer)
#             dict_id = name_dict.get(answer)
#             if dict_id == None:
#                 print ("The id is not in the collection ")
#             else: 
#                 print (f"The name for {answer} is {dict_id}")

# def main():
#     dict_count = int(input("How many pairs?"))
#     name_dict = make_dict(dict_count)
#     id_lookup(name_dict)


#main()

class TickCounter:
    def __init__(self, count = 0):
        self.count = count
        
    def tick(self):
        self.count += 1
    
    def get_count(self):
        return self.count
    
    def reset(self):
        self.count = 0



counter = TickCounter()
for _ in range(45):
    counter.tick()
print("The current count: ", counter.get_count())
for _ in range(12):
    counter.tick()
print("The current count: ", counter.get_count())
counter.reset()
for _ in range(31):
    counter.tick()
print("The current count: ", counter.get_count())




















