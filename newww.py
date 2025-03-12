def add(a, b, c, d):
    if d == 0:
        return "Error: Division by zero"
    return a + b - (c * d) 

x = 10
y = "hello"

if x > 5:
    print("X is big")

for i in range(5):
    print(f"Power of {i}: {i ** i}") 

lst = [1, 2, 3]
if len(lst) > 10:
    print(lst[10]) 

counter = 0
while counter < 5: 
    print(f"Counter: {counter}")
    counter += 1
