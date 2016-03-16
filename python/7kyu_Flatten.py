# a function that flattens an Array of Array objects into a flat Array. 
# a function must only do one level of flattening.

def flatten(lst):
    try:
        return [j for i in lst for j in i]
    except TypeError:
        return lst
		
# flatten [1,2,3] # => [1,2,3]
# flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
# flatten [[[1,2,3]]] # => [[1,2,3]]