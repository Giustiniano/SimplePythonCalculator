import re
from numbers import Number

INPUT_FORMAT = re.compile(r"-?\d+\s*[+\-*/]\s*-?\d+")


def simple_python_calculator(usr_input: str) -> Number:
    if not INPUT_FORMAT.fullmatch(usr_input):
        raise ValueError("Unable to parse string, please try again")
    return eval(usr_input.strip())

if __name__ == '__main__':
    while True:
        print("""
        Enter an arithmetical operation between two numbers, using '/' for division and '*' for multiplication, 
        '+' and '-' for addition and subtraction respectively without leading or trailing spaces, 
        otherwise press enter to exit
        """)
        user_input = input("> ")
        if not user_input:
            break
        try:
            print(simple_python_calculator(user_input))
        except ValueError as ve:
            print(str(ve))
            continue
