print("Welcome to pythonProject")

print("-------------Data Types---------------")

print("String Concatenation : ")
print("20 days are " + str(20*24*60) + " Minutes")
print("or")
print(f"20 days are {20*24*60} minutes")

print("-------------Variable-------------------")

calculation_to_seconds = 24*60*60
calculation_to_units = 24
name_of_unit = "Hour"

print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
print(f"30 days are {30 * calculation_to_seconds} seconds")
print(f"55 days are {55 * calculation_to_seconds} seconds")

print("------------Function---------------")

def days_to_unit():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("all good")
days_to_unit()

print("-----------Function Parameter--------------")
def days_to_unit(num_of_days , custom_message):
    print(f" {num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_unit(50 , "Awsome")
days_to_unit(35 , "Good")
days_to_unit(60 , "nice")
days_to_unit(100, "hmmm")

print("-----------Scop---------------")

print("Global Scop : Global variable")
print("Local Scop : local variable")

