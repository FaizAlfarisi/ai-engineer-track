# Lesson 8 — Exception Handling
# Write all exercise solutions here first, then paste each into its
# notebook cell. Do not delete or reorder these sections — the notebook
# cells must stay in sync.
#
# This file starts blank. The learner writes all code.

# --- E1 ---
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return "invalid"
    
for t in ["42", "12a", ""]:
    print(to_int(t))

# --- E2 ---
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
    except TypeError:
        return "type error"
    
print(safe_divide(10,4))
print(safe_divide(10,0))
print(safe_divide(10,"x"))

# --- E3 ---
def load_port(config):
    try:
        port = int(config["port"])
    except KeyError:
        return "missing key"
    except ValueError:
        return "not a number"
    else:
        return f"ready on {port}"
    
print(load_port({"port": "8080"}))    
print(load_port({}))    
print(load_port({"port": "abc"}))    

# --- E4 ---
def process(name, events: list):
    try:
        if name == "bad":
            raise ValueError(f"failed {name}")
    except ValueError as err:
        events.append(str(err))
    else:
        events.append(f"processed {name}")
    finally:
        events.append(f"closed {name}")
        
events = []
process("data", events)
process("bad", events)

for e in events:
    print(e)

# --- E5 ---
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount

try:
    print(withdraw(100,30))
except ValueError as err:
    print(err)
try:
    print(withdraw(100, 150))
except ValueError as err:
    print(err)

# --- M1 ---
def summarize(records: list[str]):
    s = {
        "total": 0,
        "valid": 0,
        "invalid": 0
    }
    for record in records:
        try:
            name, amount = record.split(",")
            
            if not name:
                raise ValueError("invalid name")
            
            amount = float(amount)
                        
        except ValueError:
            s["invalid"] += 1
            
        else:
            s["valid"] += 1
            s["total"] += amount

    return s

records = [
    "coffee,-3.50",
    "salary,+2500.00",
    "rent:bad",
    "",
    "-12",
    "snacks,+4.20",
]
s = summarize(records)
print(f"total: {s['total']:.2f}")
print(f"valid: {s['valid']}")
print(f"invalid: {s['invalid']}")


# --- M2 ---
def first_valid(candidates: list):
    for c in candidates:
        try:
            return int(c)
        except ValueError:
            continue

    raise ValueError("no valid input")

try:
    print(first_valid(["x", "", "7", "3"]))
except ValueError as err:
    print(err)

try:
    print(first_valid(["a", "b"]))
except ValueError as err:
    print(err)

# --- M3 ---
def load_settings(raw: dict):
    spec = {
        "retries": int,
        "rate": float, 
    }
    
    result = {
        "retries": 0,
        "rate": 0.0
    }
    
    for key, value_type in spec.items():
        try:
            result[key] = value_type(raw[key])
        except (ValueError, KeyError):
            raise ValueError(f"bad setting: {key}")
    return result

try:
    print(load_settings({"retries": "3", "rate": "0.5"}))
except ValueError as err:
    print(err)

try:
    print(load_settings({"retries": "three", "rate": "0.5"}))
except ValueError as err:
    print(err)

# --- H1 (fixed version goes here after debugging) ---
def to_celsius(text):
    return round((float(text) - 32) * 5 / 9, 1)


def read_batch(readings):
    good = []
    for r in readings:
        try:
            good.append(to_celsius(r))
        except (ValueError, TypeError):
            pass
            
    if not good: # easier check if good ever have a value
        return None
    return good


def count_skipped(readings):
    skipped = 0
    for r in readings:
        try:
            to_celsius(r)
        except (ValueError, TypeError):
            skipped += 1 # increment the skipped value
    return f"skipped: {skipped}" # change to f string


def mean(values):
    if not values: # zero division guard
        raise ValueError("no data")
    return sum(values) / len(values)


# --- driver (do not change) ---
temps = ["70", "oops", "75"]
print(read_batch(temps))
print(count_skipped(temps))
print(mean([21.1, 23.9]))
try:
    print(mean([]))
except ValueError as err:
    print(err)

# --- H2 ---
def parse_line(line: str, types: tuple):
    line = line.strip()
    
    if not line: 
        raise ValueError("empty row")
    
    lines = line.split(",")
    result = []
    
    for i in range(len(types)):
        if types[i] == str and not lines[i]:
            raise ValueError(f"bad field: {i}")
        
        try:
            result.append(types[i](lines[i]))
        
        except ValueError:
            raise ValueError(f"bad field: {i}")
        
    return tuple(result)
        
specs = (str, int, float)
try:
    print(parse_line("alice,30,1.75", specs))
except ValueError as err:
    print(err)

try:
    print(parse_line("bob,abc,1.70", specs))
except ValueError as err:
    print(err)

try:
    print(parse_line("   ", specs))
except ValueError as err:
    print(err)

# --- CHALLENGE ---
def parse_entry(line: str):
    if "," not in line:
        raise ValueError("missing comma")

    description, amount = (part.strip() for part in line.split(","))
    
    if not description:
        raise ValueError("empty description")
    
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("bad amount")

    return description, amount

def format_entry(description, amount):
    return f"{description} {amount:.2f}"

def main(lines, out=print):
    summary = {
        "rejected": 0,
        "total": 0,
        "valid": []
    }
    
    for line in lines:
        try:
            description, amount = parse_entry(line)
        except ValueError as err:
            summary["rejected"] += 1
        else:
            summary["total"] += amount
            summary["valid"].append(format_entry(description, amount))
        
    out("=== valid ===")
    out("\n".join(valid for valid in summary['valid']))
    out(f"=== rejected: {summary['rejected']} ===")
    out(f"total: {summary['total']:.2f}")
    
    return

lines = [
    "coffee,-3.50",
    "salary,+2500.00",
    "nope",
    ",5.00",
    "snack,abc",
]
main(lines)