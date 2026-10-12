"""Quiz 04 E driver — PROVIDED, do NOT modify. Run: python check_q.py"""

import qharvest as q
assert q.first_over(iter([18.0, 41.0, 19.0]), 40.0, 5) == [41.0]
assert q.first_over([45.0, 20.0, 46.0], 40.0, 1) == [45.0]
assert q.first_over(iter([]), 40.0, 3) == []

pulled = []


def src():
    for x in [1, 2, 3]:
        pulled.append(x)
        yield x


assert q.first_over(src(), 40.0, 0) == []
assert pulled == []

assert q.count_and_collect(["a", "b", "c"]) == (3, ["a", "b", "c"])
assert q.count_and_collect(iter(["a", "b"])) == (2, ["a", "b"])
assert q.count_and_collect(iter([])) == (0, [])

print("E-Q4 OK")
