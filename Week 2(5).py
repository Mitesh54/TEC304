from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]

#Square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

#Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, squared))
print("Even Squares:", even_numbers)

#Multiply all numbers
product = reduce(lambda a, b: a * b, even_numbers)
print("Product:", product)