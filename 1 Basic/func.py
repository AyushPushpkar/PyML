
# Immutable Types (like int, str) = Acts like PBV
def modify_number(n):
    print("Inside function before change:", n)
    n = n + 5
    print("Inside function after change:", n)

num = 10

modify_number(num)
print("Outside function:", num)


# Mutable Types (like list, dict) = Acts like PBR
def add_item(mylist):
    print("Before:", mylist)
    mylist.append(100)
    print("After:", mylist)

numbers = [1, 2, 3]
add_item(numbers)
print("Outside function:", numbers)

# print(add_item(numbers))

def multiply(*nums):
    res = 1
    for num in nums :
        res *= num

    return res

print(multiply(2,3,4))   



