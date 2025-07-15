a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # ✅ True → because the values are the same
print(a is b)  # ❌ False → different objects in memory

x = "hello"
y = "hello"
print(x is y)  # ✅ True in this case, because Python interns small strings

print("\n")

a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)  # ✅ True

c = a
print(a is c)  # ✅ True

a = (1, 2, [3])
b = (1, 2, [3])
print(a is b)  # ❌ False — different objects (because lists are mutable)

