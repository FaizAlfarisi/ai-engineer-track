"""DSA Week 4 — Config Audit (Stack). The learner writes ALL code here."""


def audit(s: str) -> int | None:
    pair = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    
    opener = []
    set_open = set("([{")
    set_close = set(")]}")
    for idx, item in enumerate(s):
        if item in set_open:
            opener.append((item, idx))
        
        if item in set_close:
            if not opener:
                return idx

            last, _ = opener.pop()
            
            if pair[last] == item:
                continue
            else:
                return idx
            
    if opener:
        return opener[0][1]

    return None
    
assert audit("") == None
assert audit("([{}])") == None
assert audit("([)]") == 2
assert audit("(((") == 0
assert audit("())") == 2
assert audit("a(b[c]d)e") == None