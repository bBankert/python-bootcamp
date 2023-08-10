# generators lazy load

def my_generator():
    yield 1
    yield 2
    yield 3

# destructuring
[val_1, *rest] = my_generator()

print(f"First yield value is {val_1}, rest is {rest}")

# fibonacci generator

def fib_generator(n):
    a = b = 1
    for i in range(n):
        yield a
        # equivalent to a = b & b = a + b
        a, b = b, a + b

print("Fibonacci generator")
for i in fib_generator(20):
    print(i)

