# Lesson 4 — Loops

# E1
words = ["cat", "window", "defenestrate"]
print("\n".join([f"{word}: {len(word)}" for word in words]))

# E2
total = 0
for n in range(1, 11):
    total += n
print(f"sum 1..{n} = {total}")

# E3
i = 3

while i >= 0:
    print(i)
    i -= 1
print("liftoff!")


# E4
items = ["tic", "tac", "toe"]

print("\n".join([f"{i} {item}" for i, item in enumerate(items)]))

# E5
# print("\n".join([f"{x}" for x in range(10) if x%2 != 0]))
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# M1
names = ["ada", "ben", "cyn"]
scores = [88, 92, 75]

print("\n".join(f"{name}: {score}" for name, score in zip(names, scores)))

# M2
words = ["Data", "data", "is", "IS", "gold"]
normalized_word = [word.lower() for word in words]
# normalized_word = list(map(str.lower, words))

word_counts = {}
for word in normalized_word:
    word_counts[word] = word_counts.get(word, 0) + 1
    
print("\n".join([f"{word}: {count}" for word, count in word_counts.items()]))

# M3
items = ["ada", "ben", "cyn"]

# Path 1
target_1 = "ben"
for i, item in enumerate(items):
    if item == target_1:
        print(f"found: {item} at {i}")
        break
else:
    print(f"not found: {target_1}")

# Path 2
target_2 = "zoe"
for i, item in enumerate(items):
    if item == target_2:
        print(f"found: {item} at {i}")
        break
else:
    print(f"not found: {target_2}")
        

# H1
# Goal: sum 1..10, remove every "b" from a list, and countdown 3..0 then "liftoff!".
total = 0
for n in range(1, 10+1): # add 1 to the range
    total += n
print(f"sum = {total}")

items = ["a", "b", "b", "c"]
for item in items.copy(): # copy the items list
    if item == "b":
        items.remove(item)
print(items)

count = 3
while count >= 0: # add equal
    print(count)
    count -= 1
print("liftoff!")

# H2
result = []
for n in range(1, 11):
    if n % 2 == 0:
        result.append(n ** 2)
print(result)

result_comp = [n**2 for n in range(1, 11) if n%2 == 0]
print(result_comp)
print(f"equal: {bool(result == result_comp)}")

names = ["cat", "window"]

name_counts = {name: len(name) for name in names}
print(name_counts)

# CHALLENGE
class_size = input("Enter class size: ")
if not class_size.isdigit() or int(class_size) < 1:
    print("invalid size -> set to 3")
    class_size = 3
else:
    class_size = int(class_size)

total_score = 0
total_pass = 0
highest = None
lowest = None
distribution = {}
    
print("=== GRADEBOOK ===")    
    
for i in range(1, class_size+1):
    name = input(f"Enter name #{i}: ") 
    score_input = input(f"Enter score #{i}: ") 
    
    if not name:
        print("empty name -> set to 'unknown'")
        name = "unknown"
    
    if not score_input.isdigit() or not 0 <= int(score_input) <= 100:
        print(f"invalid score for {name} -> set to 50") 
        score = 50
    else:
        score = int(score_input)
        
    total_score += score
    
    if highest is None or score > highest:
        highest = score
    if lowest is None or score < lowest:
        lowest = score
        
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    if score >= 40:
        status = "pass"
        total_pass += 1 
    else:
        status = "fail"
        
    distribution[grade] = distribution.get(grade, 0) + 1
        
    print(f"{i}. {name} - {score} - {grade} - {status}")
        
print("=== SUMMARY ===")
print(f"students: {class_size}")
print(f"average: {(total_score / class_size):.2f}")
print(f"highest: {highest}")
print(f"lowest: {lowest}")
print(f"pass rate: {(total_pass / class_size * 100):.1f}%")

print("=== DISTRIBUTION ===")    
for grade in "ABCDF":
    count = distribution.get(grade, 0)
    if count:
        print(f"{grade}: {count}")