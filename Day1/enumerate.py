""" We can use enumerate function to get the 
    the counter and the value of the iteratable at the same time
"""
ls = ["Omar", "Enumerate", "Function"]
for count, value in enumerate(ls):
    print(count, value)

print("---" * 10)

# We can also define a starting value for the counter
for count, value in enumerate(ls, start=3):
    print(count, value)
