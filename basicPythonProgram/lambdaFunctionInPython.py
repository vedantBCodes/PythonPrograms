"""

In Python, lambda functions are small anonymous functions, defined with the lambda keyword.
They are often used when you need a simple function for a short period of time,
without defining a full function using def.

Syntax :

lambda arguments: expression

Arguments: The lambda function can take any number of arguments, separated by commas.
Expression: This is the single expression that gets evaluated and returned when the lambda function is called.

"""

# Example 1: Simple Lambda Function

# Lambda function to add 10 to a number
add_ten = lambda x: x + 10

print(add_ten(5))  # Output: 15

# Example 2: Lambda Function with Multiple Arguments

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y

print(multiply(3, 4))  # Output: 12


# Example 3: Using Lambda with map, filter, and sorted

# Using with map: Applies a lambda function to each element in an iterable.

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

# Using with filter: Filters elements based on a condition defined in the lambda.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]