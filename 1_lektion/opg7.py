def divide(a, b=1):
    try:
        return a // b
    except ZeroDivisionError:
        return 0

print(divide(4, 2))
print(divide(4, 0))
print(divide(4))