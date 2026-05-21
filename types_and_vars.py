# types_and_vars.py
# Demonstrating variables, types, printing, and basic arithmetic

# --- Basic Variables ---
name = "Henry"          # string variable
age = 57                # integer variable
height = 1.80           # float variable (meters, converted from 5' 11")

# --- Introduction Sentence ---
print(f"Hello, my name is {name}. I am {age} years old and {height} meters tall.")

# --- Age in 5 Years ---
# Calculate future age using addition
future_age = age + 5
print(f"In 5 years, I will be {future_age} years old.")

# --- Rectangle Area ---
# Demonstrating multiplication operator
width = 5.5
height_rect = 2
area = width * height_rect
print(f"The area of a {width} x {height_rect} rectangle is {area}.")

# --- Demonstrating Operators ---
sum_example = age + 10          # addition
mod_example = age % 4           # modulus operator
repeat_string = name * 3        # string repetition

print(f"Age + 10 = {sum_example}")
print(f"Age % 4 = {mod_example}")
print(f"Repeating my name 3 times: {repeat_string}")
