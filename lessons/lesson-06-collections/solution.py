# Lesson 6 — Collections
# Write all exercise solutions here first, then paste each into its notebook cell.
# Do not delete or reorder these solutions — the notebook cells must stay in sync.

# E1
original = [1,2,3]
alias = original
copy = original.copy()

alias.append(99)
copy.append(7)
print(f"original: {original}")
print(f"alias: {alias}")
print(f"copy: {copy}")

# E2
a, b = 3, 7
b, a = a, b
print(a, b)

def min_max(nums):
    return (min(nums), max(nums))

lo, hi = min_max([4, 9, 2])
print(lo, hi)

# E3
names = ["ada", "ben"]
scores = {"ada": 92, "ben": 88}
unique = {92, 88}
print("ada" in names)
print("cyn" in names)
print("ada" in scores)
print(92 in scores)
print(92 in scores.values())
print(92 in unique)

# E4
counts = {}
word = "banana"

for ch in word.lower():
    counts[ch] = counts.get(ch, 0) + 1

print(counts)

# E5
nums = [3,1,3,2,1,4]

copied = nums.copy()
print(sorted(set(copied)))

# M1
group_a = {"ada", "ben", "cyn"}
group_b = {"ben", "dan", "ela"}

print(f"intersection: {sorted(group_a & group_b)}")
print(f"union: {sorted(group_a | group_b)}")
print(f"a - b: {sorted(group_a - group_b)}")
print(f"symmetric diff: {sorted(group_a ^ group_b)}")

# M2
groups = {}
students = [("ada", "eng"), ("ben", "ai"), ("cyn", "eng"), ("dan", "ai"), ("ela", "ai")]

for name, dept in students:
    groups.setdefault(dept, []).append(name)

groups

# M3
matrix = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
    ]

rows = matrix.copy()
cols = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(f"rows: {rows}")
print(f"cols: {cols}")

# H1
nums = [3, 1, 3, 2]
saved = set()
for n in nums:
    saved.add(n)         # BUG 1: this is assignment, not adding
print(saved)

uniq = set()                  # BUG 2: this is a dict, not a set
uniq.add(5)
print(uniq)

word = "Banana"
counts = {}
for ch in word.lower():
    counts[ch] = counts.get(ch, 0) + 1
print(counts)              # BUG 3: 'B' and 'b' counted separately

a, b = 5, 8
a, b = b, a                # BUG 4: this is not a swap
print(a, b)

# H2
def two_sum(numbers: list, target: int):
    seen = set()
    result = None
    for num in numbers:
        residual = target - num
    
        if residual in seen:
            if residual < num:
                result = (residual, num)
            else:
                result = (num, residual) 
            break
    
        seen.add(num)
    return result
    
print(two_sum([3,5,2,7], 10))
print(two_sum([1,2,3], 9))

# CHALLENGE
def add_product(products: dict, name, price, qty, category):
    if name in products:
        return f"exists: {name}"
    else:
        products[name] = {
            "price": price,
            "qty": qty,
            "category": category
        }
        return 

def restock(products: dict, name, qty):
    if name in products:
        products[name]['qty'] += qty
        return 
    else:
        return f"unknown: {name}"

def sell(products, name, qty):
    if name in products:
        if qty > products[name]['qty']:
            return f"insufficient: {name} has {products[name]['qty']}"
        else:
            products[name]['qty'] -= qty
        return 
    else:
        return f"unknown: {name}"

def report(products: dict):
    print("=== inventory ===")
    total_value = 0
    categories = set()
    for name in products:
        qty = products[name]['qty']
        price = products[name]['price']
        category = products[name]['category']
        categories.add(category)
        value = qty * price
        total_value += value
        
        print(f"{name}: {qty} x {price:.2f} = {value:.2f} ({category})")
        
    print(f"total value: {total_value:.2f}")
    cat_list = sorted(categories)
    print(f"categories: {" ".join(cat_list) if cat_list else 'none'}")
    
    low_stock = [name for name, product in products.items() if product['qty'] < 5]
    print(f"low stock: {" ".join(low_stock) if low_stock else 'none'}")

def main():
    products = {}
    while True:
        command = tuple(input().strip().lower().split())
        
        match command[0]:
            case "add":
                name, price, qty, category = command[1:]
                if not price.replace(".", "").isdigit() or float(price) <= 0 or not qty.isdigit() or int(qty) <= 0:
                    print(f"invalid: {name}")
                    continue
                price = float(price)
                qty = int(qty)
                add = add_product(products, name, price, qty, category)
                print(add if add else f"added: {name}")
            case "restock":
                name, qty = command[1:]
                if not qty.isdigit() or int(qty) <= 0:
                    print(f"invalid: {name}")
                    continue
                qty = int(qty)
                restock_product = restock(products, name, qty)
                print(restock_product if restock_product else f"restocked: {name} -> {products[name]['qty']}")
            case "sell":
                name, qty = command[1:]
                if not qty.isdigit() or int(qty) <= 0:
                    print(f"invalid: {name}")
                    continue
                qty = int(qty)
                sell_product = sell(products, name, qty)
                print(sell_product if sell_product else f"sold: {name}, left {products[name]['qty']}")
            case "report":
                report(products)
            case "quit":
                break
            case _:
                break
main()