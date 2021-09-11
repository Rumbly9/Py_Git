def calc_type(a, b, res):
    if a + b == res:
        return "addition"
    elif abs(a - b) == res:
        return "subtraction"
    elif a * b == res:
        return "multiplication"
    else:
        return "division"

# cleaner version

def calc_type_clean(a, b, res):
    return {
        a + b: "addition",
        a - b: "subtraction",
        a * b: "multiplication",
        a / b: "division"
        }[res]
