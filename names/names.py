import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ^^^ Runtime: O(n^2) ^^^


duplicates = []
# bst = BinarySearchTree(names_1[0])

# # O(n)
# for name in names_1[1:]:
#     bst.insert(name)

# # O(n)
# for name in names_2:
#     # O(n*log(n))
#     if bst.contains(name):
#         duplicates.append(name)

# create sets from names
set1 = set(names_1)
set2 = set(names_2)

# run intersection method to return duplicates
duplicates = set1.intersection(set2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
