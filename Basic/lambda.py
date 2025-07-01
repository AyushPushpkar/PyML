
def sum_of_squares(nums):
    squared = map(lambda x: x * x, nums)  # Square each number
    total = sum(squared)                  # Sum of squares
    return total

# Example usage
nums = [1 ,2 ,3 ,4 ]
result = sum_of_squares(nums)
print("Sum of squares:", result)


square = lambda x : x**2
squared_num = list(map(square,nums))
print(squared_num)




first_name = ["clover" , "alby"]
last_name = ['hank' , 'sobek']

full_name = list(zip(first_name,last_name))
print(full_name)

