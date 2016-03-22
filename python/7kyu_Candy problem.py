
def candies(s):
    return -1 if len(s) <= 1 else sum([max(s) - i for i in s if i != max(s)])

# candies ([5,8,6,4]) # return 9
# candies ([1,2,4,6]) # return 11
# candies ([1,6]) # return 5
# candies ([]) # return -1
# candies ([6]) # return -1 (because only one kid)