#CD
answer = str(input())
count_list = answer.strip().split()
first_set = set()
second_set = set()
first_counter = int(count_list[0])
second_counter = int(count_list[1])

counter = 0
answer = str(input())

while answer != "0 0" and (counter <= (first_counter + second_counter)):
    answer = int(answer)
    if counter <= first_counter:
        first_set.add(answer)
    elif counter <= (first_counter + second_counter):
        second_set.add(answer)
    counter +=1
    answer = str(input())
    

shared_count = (first_set.intersection(second_set))

print (len(shared_count))