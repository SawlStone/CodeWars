def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal += (principal * (interest - (interest * tax)))
        year += 1
    return year