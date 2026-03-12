#find the factorial of a number.
def factorial_of_number(n):
    if n == 0:
        return 1
    else:
        return n * factorial_of_number(n-1)
number = 5
print(factorial_of_number(number))
#find largest element in a list
def largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
numbers =[1,2,3,4,5,6,7,8,9]
print(largest_element(numbers))

# smallest element in arr
def smallest_element(lst):
    smallest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
    return smallest
numbers =[1,2,3,4,5,6,7,8,9]
print(smallest_element(numbers))
# function to calculate string length
def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count
string = "hello world"
print(string_length(string))
# find second largest element in a list
def second_largest_element(lst):
    largest = max(lst)
    second_largest = min(lst)
    for num in lst:
        if num > second_largest and num < largest:
            second_largest = num
    return second_largest
numbers =[1,2,3,4,5,6,7,8,9]
print(second_largest_element(numbers))