calculate_to_units = 24
name_of_unit = "hours"

def days_to_unit (num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "You entered a 0 , Please enter a valid positive number "

def validate_and_execute():

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0 , Please enter valid positive number")
        else:
            print("your input is not a valid number . Don't ruin my Program")

user_input = input("Hey user, Enter a number of days and i will convert it to hours ! \n")
validate_and_execute()
