# Validate Name and Age

def main():
    name = get_name()
    age = get_age()
    print (f"Nice to meet you {name}.")
    print (f"Congratulations on your {age} years.")

def get_name() -> str:
    while True:
        name = input("What's your name? ")
        if all(c.isalpha() or c.isspace() for c in name) and any(c.isalpha() for c in name):
            return name
        else:
            print ("Please enter a valid name.")

def get_age() -> str:
    while True:
        age_str = input("How old are you? ")
        try:
            age_test = int(age_str)
            if 0 <= age_test <= 125:
                return age_str
            else:
                print (f"You seriously expect me to believe you are {age} years old?")
        except ValueError:
            print ("Please enter an integer.")


if __name__ == "__main__":
    main()