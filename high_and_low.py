def high_and_low(numbers):
    res = [int(num) for num in numbers.split()]
    return "{} {}".format(max(res), min(res))