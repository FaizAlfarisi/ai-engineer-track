# Lesson 2 — Operators & Strings
# Final answers live here. One section per exercise (e1..h2) + challenge.

# E1
print(f"14 -> {2 + 3 * 4}")
print(f"512 -> {2 ** 3 ** 2}")
print(f"8 -> {10 - 4 + 2}")
print(f"2 -> { 7 % 3 + 1}")
print(f"4.0 -> {2 * 3 - 4 / 2}")
print(f"False -> {not True or False and True}")

# E2
for _ in range (int(input("input ur total test case: "))):
    number = int(input(""))
    print(f"n={number} -> {0 <= number <= 100}")

# E3
s = "algorithm"
substrings = ["algo", "rith", "xyz", ""]
print("\n".join(f"'{substring}' {"in" if substring in s else "not in"} '{s}'" for substring in substrings))

# E4
print("  jOnA  ".strip().title())
print("bottle".strip("bo"))
# strip("bo") will delete the string b and o

# E5
s = "python"
print(f"first3: {s[:3]}")
print(f"last3: {s[3:]}")
print(f"reversed: {s[::-1]}")
print(f"every2nd: {s[::2]}")
print(f"mid: {s[1:4]}")

# M1
sentence = "The quick brown fox jumps over the lazy dog"
print(f"words: {len(sentence.split())}")
print(f"non-space chars: {len(sentence.replace(" ", ""))}")

# M2
text = "Data Is the New Oil"
print(f"lower: {text.lower()}")
print(f"upper: {text.upper()}")
print(f"title: {text.title()}")
print(f"count of 'i': {text.lower().count("i")}")

# M3
words = ["radar", "Racecar", "hello", "madam"]
print("\n".join(f"{word}: {word[::-1].lower() == word.lower()}" for word in words))

# H1
word = "  python  "
word.strip() # word.strip() is not tagged into a variable, so that the next usage of string word will not effected by strip() method
upper_word = word.upper().strip() # either applying the string method in one expression or using the variable name from word.strip()
print("clean:", upper_word) 
contains_th = word.count("th") # using the upper_mean using the string word that been uppercased, so that there is no 'th' (lowercase) in the word, it should be using the variable word
print("contains 'th':", bool(contains_th))
is_python = upper_word == "PYTHON"
print("is 'PYTHON':", is_python)

# H2
sentence = "Data science is the best"
print(" ".join(sentence.split()[::-1]))

# Challenge
prompt = """
The system will parse prompt to execute the script. However, since prompt 
contains an uppercase string, it creates a mismatch with the target function. If 
engineers process PROMPT without sanitizing it first, the runtime environment 
will reject the input. Therefore, we must never pass prompt directly into the 
compiler; instead, we should reformat prompt before deployment.
"""
print(f"words: {len(prompt.split())}")
print(f"chars (no spaces): {len(prompt.replace(" ", ""))}")
print(f"reversed: {prompt[::-1]}")
target = input("What is the target word?").lower()
print(f"{target} count: {prompt.lower().count(target)}")
print(f"redacted: {prompt.replace(target.lower(), "***").replace(target.upper(), "***").replace(target.title(), "***")}")
cleaned_prompt = prompt.lower().split()
most_common_word = max(cleaned_prompt, key=cleaned_prompt.count)
count = cleaned_prompt.count(most_common_word)
print(f"most common: '{most_common_word}' (appears {count} times)")