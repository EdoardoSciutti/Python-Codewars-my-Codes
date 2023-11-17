def narcissistic(value):
    value_str = str(value)
    num_digits = len(value_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in value_str)
    return sum_of_powers == value