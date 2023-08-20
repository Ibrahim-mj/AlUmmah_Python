user_input = input('Please enter your weight in kilogram:\n')

print(f"You said your weight is: {user_input}kg")

weight = int(user_input)

user_input = input('Please enter your height in meters:\n')

print(f"You said your height is: {user_input}m")

height = float(user_input)

body_mass_index = weight/(height*2)

print(round(body_mass_index, 2)) # round(number to round, number of places intended)
