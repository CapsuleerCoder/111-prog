#Number Validation


def is_float(string_to_test):
    try:
        float(string_to_test)
        return True
    except ValueError:
        return False


is_float(input())