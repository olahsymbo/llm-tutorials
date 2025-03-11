import random
def a():
  x = random.randint(1, 10)
  y = random.randint(1, 10)
  z = x + y
  print("Sum", z)
def b():
  x = random.randint(1, 10)
  print("Random Number", x)
def c(): print("Hello World"); d()
def d():
    for i in range(5): print(i, end = ' '); print()
def e(): pass
a();b();c();d();e()
