def multiply_once(a, b):
    return a * b

def multiply_n_iterations(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result

a = int(input("Enter 'a' for a*b: "))
b = int(input("Enter 'b' for a*b: "))

print("1 iteration:", multiply_once(a, b))
print("N iteration:", multiply_n_iterations(a, b))