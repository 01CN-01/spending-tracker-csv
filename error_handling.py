from datetime import datetime

def int_checker(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Use a Number.")

def input_checker(prompt):
    while True:
        answer = input(prompt)
        if answer != "":
            return answer
        else:
            print("Cannot Leave Blank.")

def date_format_checker(prompt):
    while True:
        try:
            date = input(prompt).strip() #Remove Spaces
            date_check = datetime.strptime(date, "%-d/%m/%Y")
            return date_check
        except ValueError:
            print("Please use this format (DD/MM/YYYY)")

def round_checker(prompt):
    while True:
        try:
            answer = float(input(prompt))
            return round(answer, 2)
        except ValueError:
            print("Invalid")