""" Lambda expressions is another way to create a function
    on the fly using the keyword 'lambda'
"""

# Simple lambda function example to simulate a power funciton
""" The following expression simply means that power_lambda is
    a function that takes two arguments and returns the a value
    equals to the first argument raised to the power of the second
"""
# power_lambda = lambda x, y: x**y  --> pep8 doesn't like this expression :D
def power_lambda(x, y): return x**y


print(power_lambda(3, 3))


""" One of the most important uses of lambda expressed functions is
    with map() functions, because it provides a function on the fly
"""
ls = [4, 5, 10, 20, 34]
squared_list = map(lambda num: num ** 2, ls)
print(list(squared_list))
