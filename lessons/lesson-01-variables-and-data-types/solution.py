# e1
name = "Faiz"
age = 22

print(f"My name is {name} and I am {age} years old.")

# e2
stop = True
print(type(age))
print(type(name))
print(type(stop))

# e3
# type(3.0) is float
# type(3) is int
# type("3") is str
print(f"type(3.0) is {type(3.0)}, type(3) is {type(3)}, type('3') is {type("3")}")

# e4
a, b = 5, 10
a, b = b, a
print(a, b)

# e5
greeting = "hello"
print(len(greeting))
print(greeting[0])
print(greeting[-1])

# m1
width = int(input("Gimme the width of the rectangle"))
height = int(input("Gimme the height of the rectangle"))
print(f"width = {width}, height = {height}, area = {width*height}, perimeter = {2*(width+height)}")

# m2
age = int(input("What is ur age?"))
print(f"Ur age in days is {age*365}")

# m3
bill = float(input("How much ur bill?"))
percentage = float(input("How much u wanna gimme a tip (in percentage)?"))
tip = bill * (percentage/100)
total = tip + bill
print(f"bill = {bill:.2f}, tip_percentage = {percentage:.2f}, tip = {tip:.2f}, total = {total:.2f}")

# h1
values = [1, 2.5, "3", True, None]
for value  in values:
    print(f"{value} -> {type(value)}")
    
    # type(True) is bool, The reason its type is bool is that True is an instance of the bool class, which subclasses int.

# h2
for i in range(1,16):
    is_even = i % 2 == 0
    
    label = (i % 3 == 0) * 'fizz' + (i % 5 == 0) * 'buzz' or str(i)
    
    print(f"{i} {is_even} {label}")
    
    
# exercise
name = input("What is ur name?")
age = int(input("How old r u?"))
height = float(input("What is ur height in 'meter' not 'american scale'?"))
is_student = True if input("R u a student? y/n") == 'y' else False

print(f'''
=== PROFILE ===
Name: {name}
Age: {age} ({age * 365} days old)
Height: {height:.2f} m ({(height * 100):.2f} cm)
Student: {is_student}
Types: {type(name).__name__}, {type(age).__name__}, {type(height).__name__}, {type(is_student).__name__}
''')