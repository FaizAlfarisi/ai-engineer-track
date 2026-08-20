# Lesson 5 — Functions
# Learner's answers live in solution.py (never pre-filled by the system).
# E1
def greet(name):
    return f"Hello, {name}!"

hello_ada = greet("ada")
print(hello_ada)
hello_owi = greet("owi")
print(hello_owi)
hello_wowo = greet("wowo")
print(hello_wowo)

# E2
def add_print(a, b):
    print(a+b)

def add_return(a, b):
    return a+b

from_print = add_print(2,3)
print(f"stored: {from_print}")
from_return = add_return(2,3)
print(f"returned: {from_return}")

# E3
def greet(name, greetings="Hello"):
    return f"{greetings}, {name}!"

hello_ben = greet("ben")
print(hello_ben)
yo_cyn = greet("cyn", "Yo")
print(yo_cyn)

# E4
def min_max(a, b):
    if a < b:
        return a, b
    return b, a

min, max = min_max(3, 9)
print(f"min_max(3, 9): low={min} high={max}")
min, max = min_max(7, 1)
print(f"min_max(7, 1): low={min} high={max}")
        

# E5
keyword_arg = greet(greetings="Hi", name="ada")
print(keyword_arg)

# M1
# part a
def increment(count):
    return count + 1

counter = increment(0)
print(counter)
counter = increment(counter)
print(counter)
counter = increment(counter)
print(counter)

# part b
n = 10
def local_n():
    n = 99
    return n
result_def = local_n()
print(result_def)
print(n)

# M2
def clean(text: str):
    """Return stripped and lowered string"""
    return text.strip().lower()

def count_word(text, word):
    return clean(text).count(word.lower())

text = "  The CAT sat ON the mat  "
countword = count_word(text, "the")
print(f"exacly {countword}")

# M3

# part a
# predicted: ["a"]
# predicted: ["a", "b"]

def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item("a"))
print(add_item("b"))

# H1
def double(x):
    return x * 2 # change print to return

def log_message(msg, history=None): # set the history from empty list to None
    if history is None:
        history = []
    history.append(msg)
    return history

def count_up(n):
    nums = []
    for i in range(1, n+1): # add clasic +1 for the boundary
        nums.append(i)
    return nums

print(double(21))
print(log_message("one"))
print(log_message("two"))
print(count_up(5))

# H2

def mean(nums):
    total = 0
    for n in nums:
        total += n
    return total / len(nums)

def min_of(nums):
    lowest = nums[0]
    for n in nums:
        if n < lowest:
            lowest = n
    return lowest

def max_of(nums):
    highest = nums[0]
    for n in nums:
        if n > highest:
            highest = n
    return highest

scores = [88, 92, 45, 30]

print(f"mean: {mean(scores)}")
print(f"min: {min_of(scores)}")
print(f"max: {max_of(scores)}")


# Challenge
def validate_size(raw: str):
    """Validate input is digit and a positive number, return int"""
    if not raw.isdigit() or int(raw) < 1:
        print("invalid size -> set to 3")
        raw = 3
    else:
        raw = int(raw)
    return raw

def read_student(i):
    """Read input user, validate empty name and score, return tuple (name, score)"""
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
    
    return name, score

def compute_grade(score):
    """Mapping the score to a grade, return str grade"""
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
    
    return grade

def is_pass(score):
    """Check status based on score, return bool"""
    return score >= 40

def main():
    class_size = input("Enter class size: ")
    class_size = validate_size(class_size)

    total_score = 0
    total_pass = 0
    highest = None
    lowest = None
    distribution = {}
        
    print("=== GRADEBOOK ===")    
    for i in range(1, class_size+1):
        name, score = read_student(i)
        grade = compute_grade(score)
        status_pass = is_pass(score)
        
        if status_pass:
            total_pass += 1
        total_score += score
        
        if highest is None or score > highest:
            highest = score
        if lowest is None or score < lowest:
            lowest = score
            
        distribution[grade] = distribution.get(grade, 0) + 1
            
        print(f"{i}. {name} - {score} - {grade} - {"pass" if status_pass else "fail"}")
            
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
    
main()