calculate_to_units = 24
name_of_unit = "hours"

def days_to_unit (num_of_days):

        return f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0 , Please enter valid positive number")

    except ValueError:

        print("your input is not a valid number . Don't ruin my Program")


user_input = input("Hey user, Enter a number of days and i will convert it to hours ! \n")
validate_and_execute()
