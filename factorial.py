def factorial(num):
    if num == 0:
        return 1
    return factorial(num-1) * num
num = 5
print(f"factorial of {num} is {factorial(num)}",)
