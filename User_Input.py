calculate_to_units = 24
name_of_unit = "hours"

def days_to_unit (num_of_days):
    return f"{num_of_days} days are {num_of_days * calculate_to_units} {name_of_unit}"

user_input = input("Hey user, Enter a number of days and i will convert it to hours ! \n")
user_input_number = int(user_input)

calculated_value = days_to_unit(user_input_number)
print(calculated_value)