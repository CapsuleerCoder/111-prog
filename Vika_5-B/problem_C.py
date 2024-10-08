#Safe Division

def main():
    try:
        string_1 = float(input())
        string_2 = float(input())
    except ValueError:
        print ("None")
        return None
    print (divide_safe(string_1, string_2))
    
def divide_safe(num1_str, num2_str):
    try:
        return round(num1_str/num2_str, 5)
    except ZeroDivisionError:
        return None

main()