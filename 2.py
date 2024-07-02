def getSum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


numbers = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
    numbers.append(element)


sum = getSum(numbers)
print("Sum of numbers is : ",sum)