# We have the number 12385. We want to know the value 
# of the closest cube but higher than 12385. 
# The answer will be 13824.

# Now, another case. We have the number 1245678. 
# We want to know the 5th power, 
# closest and higher than that number. 
# The value will be 1419857.

def find_next_power(val, pow_):
    return (int(val**(1/pow_))+1)**pow_
    # return (int(val**(1/float(pow_)))+1)**pow_    ---- for python 2.

	
# find_next_power(12385, 3) == 13824
# find_next_power(1245678, 5) == 1419857