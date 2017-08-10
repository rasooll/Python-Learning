def calculate_exponent(a, b):
    if b == 0:
        return 1
    else:
        return a * calculate_exponent(a, b-1)