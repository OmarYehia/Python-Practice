import operator

""" The operator module provide functions which are similar to
    to default python's operators
"""

print(operator.add(1, 2))
print(operator.mul(1, 2))
print(operator.eq(1, 2))
print(operator.ne(1, 2))
print(operator.mod(1, 2))

""" I think the most popular usage for this module is when you want
    to sort a list of tuples with the a certain element in the list
"""
ls = [("Omar", 5), ("Mohammed", 1), ("Mahmoud", 6), ("Sarah", 3)]
ls.sort(key=operator.itemgetter(1))
print(ls)
