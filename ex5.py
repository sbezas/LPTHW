name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
weight_in_kg = round(weight / 2.2,2)
height_in_cm = height * 2.54

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_in_cm} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kg} kilograms heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
