# E1
# 0 -> False
print(f"{0!r} -> {bool(0)}")

# 0.0 -> False
print(f"{0.0!r} -> {bool(0.0)}")

# "" -> False
print(f"{""!r} -> {bool("")}")

# "0" -> True
print(f"{"0"!r} -> {bool("0")}")

# [] -> False
print(f"{[]!r} -> {bool([])}")

# " " -> True
print(f"{" "!r} -> {bool(" ")}")

# [0] -> True
print(f"{[0]!r} -> {bool([0])}")

# None -> False
print(f"{None!r} -> {bool(None)}")

# False -> False
print(f"{False!r} -> {bool(False)}")

# E2
# your code here

test_numbers = [-5, 0, 42]

for test_number in test_numbers:
    if test_number == 0:
        sign = "zero"
    elif test_number > 0:
        sign = "positive"
    else:
        sign = "negative"
    print(f"{test_number} -> {sign}")

# E3
# your code here
test_numbers = [-5, 42, 100]
print("\n".join(f"n={n} -> {'even' if n % 2 == 0 else 'odd'} -> {'in range' if 0 <= n <= 100 else 'out of range'}" for n in test_numbers)) 
# i can do it in a single line but it seem to be not readable haha, gimme some advice to decide how to code effectively and efficiently without losing its readability
# E4
# your code here

test_names = ["", "ue", "faiz"]
for name in test_names:
    if not name:
        print("invalid: empty name")
    elif len(name) < 2:
        print("invalid: too short")
    else:
        print(f"ok: Hello, {name}")


# E5
# your code here
commands = ["start", "stop", "pause", "start"]

for command in commands:
    match command:
        case "start": 
            print(f"{command} -> starting")
        case "stop": 
            print(f"{command} -> stopping")
        case _: 
            print(f"{command} -> unknown command")

# M1
# your code here
scores = [101, 100, 85, 60, 59]

for score in scores:
    if not (0 <= score <= 100):
        print("invalid score")
        continue
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Score: {score} -> grade {grade}")

# M2
# your code here
cases = [(True, 120.0, False), (True, 50.0, True), (True, 50.0, False), (False, 250.0, False), (False, 100.0, False)]

for case in cases:
    member, spend, referred = case
    if member and (spend >= 100 or referred):
        discount = 20
    elif not member and spend >= 200:
        discount = 10
    else:
        discount = 0
    print(f"member={member} spend={spend} referred={referred} -> {discount}%")

# M3
# your code here
for code in [200, 201, 400, 404, 500, 503, 418]:
    match code:
        case 200 | 201:
            label = "ok"
        case 400 | 404: # move the 404 case into this level
            label = "client error"
        case 500 | 503:
            label = "server error"
        case _:
            label = "unknown"
    print(f"{code} -> {label}")

# H1
# your code here
score = int(input("Enter score: ")) # convert the input type into int
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
print(f"grade: {grade}")
print(f"result: pass" if score >= 40 else "result: fail")
# if grade == "A" or grade == "B": # change the 'and' operator into 'or'
#     print("result: pass")
# else:
#     print("result: fail")

# H2
# your code here
entries = [("INFO", 5), ("WARNING", 2), ("ERROR", 3), ("CRITICAL", 9), ("DEBUG", 0), ("UNKNOWN", 1)]

for severity, count in entries:
    match severity:
        case "CRITICAL" | "ERROR" if count >= 5:
            message = "alert on-call" 
        case "CRITICAL" | "ERROR":
            message = "log to error file"
        case "WARNING":
            message = "log to warning file"
        case "INFO" | "DEBUG":
            message = "log to info file"
        case _:
            message = "drop"
    
    print(f"{severity}({count}) -> {message}")
    
    
# Challenge
# your code here

test_cases = [("CRITICAL", "login", "8"), ("urgent", "", "99"), ("high", "billing", "4"), ("low", "crash", "10")]
priorities = ["low", "medium", "high", "critical"]

for priority, category, agent_load in test_cases:
    priority = priority.strip().lower()
    category = category.strip().lower()
    # stage 1 
    print("=== TICKET VALIDATION ===")
    if priority not in priorities:
        priority = "low"
        print("invalid priority -> set to 'low'")
    if not category:
        print("empty category -> set to 'general'")
        category = "general"
    if not agent_load.isdigit() or not 0 <= int(agent_load) <= 10:
        print("invalid load -> set to 5")
        agent_load = 5
    else:
        agent_load = int(agent_load)

    # stage 2
    match (priority, category):
        case ("critical", _) if agent_load >= 8:
            routing_message = "ON-CALL TEAM"
        case (_, "login" | "auth"):
            routing_message = "auth team"
        case (_ , "billing" | "payment"):
            routing_message = "finance team"
        case (_ , "crash" | "bug"):
            routing_message = "engineering team"
        case (_ , _):
            routing_message = "general team"

    print(f"priority: {priority}")
    print(f"category: {category}")
    print(f"load: {agent_load}")
    print("=== ROUTING ===")
    print(f"team: {routing_message}")

