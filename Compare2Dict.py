# Python3 code to demonstrate working of
# Compare Dictionaries on certain Keys
# Using loop

# initializing dictionaries
test_dict1 = {'gfg': 2, 'is': 2, 'best': 3, 'for': 4, 'geeks': 5}
test_dict2 = {'gfg': 2}

# printing original dictionaries
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))

# initializing compare keys
comp_keys = ['best', 'geeks']

# Compare Dictionaries on certain Keys
# Using loop
res = True
for key in comp_keys:
    if test_dict1.get(key) != test_dict2.get(key):
        res = False
        break

    # printing result
print("Are dictionary equal : " + str(res))