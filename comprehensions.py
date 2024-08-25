# old_list = "abcde"
# new_list = [
#     c.upper() if c in "aeiou" else c
# for i, c in enumerate(old_list) if i % 2 == 0
# ]
# print(new_list)


# print([(i, j) for i in range(5)
# if i > 2 for j in range(i) if j < 2])


# print({i: c for i, c in enumerate("abcaebce") if i < 5})


# arr = [("a", 1), ("b", 2), ("c", 2)]
# for idx, (char, i) in enumerate(arr):
#     print(idx, char, i)
# print([{key: value, "i": idx}
# for idx, (key, value) in enumerate(arr)])


d = {"a": 1, "b": 2, "c": 3}
print([(k, v) for k, v in d.items()])

print([(a, b, c) for a, b, c in zip([1, 2, 3], [4, 5, 6], [7, 8, 9])])
