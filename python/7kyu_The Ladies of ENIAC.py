def rad_ladies(name):
    return str("".join([i for i in name if i not in "%$&/£?@1234567890"]).upper())