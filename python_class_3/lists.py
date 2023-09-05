# List of integer numbers
numbers = [1, 2, 3, 4, 5]

# list for storing strings
fruits = ["apple", "banana", "orange"]

# mix list
mixed = [1, 2, 3, "four", "five", "six", 3.14, None]


# Accessing list elements using indexing
# Indexing starts from 0
print(numbers[0])
print(fruits[1])
print(mixed[3])


print(f"Original list of fruits is {fruits}")
print(f"Original list of numbers is {numbers}")
print(f"Original list of mixed is {mixed}")

# moficationof number list
fruits[0] = "mango"

#  --------------- Functions on list integrates ---------------- #
# length of list

numbers_len = len(numbers)
print(numbers_len)

# min and max -> function to get minimum and maximum number in list
min_num = min(numbers)
print(f"Minimum number in list is {min_num}")


max_number = max(numbers)
print(f"Maximum number in list is {max_number}")


# sum -> function to get sum of all numbers in list
total_in_numbers = sum(numbers)
print(f"Sum of numbers in list is {total_in_numbers}")


# append -> function to add element at the end of list
fruits.append("grapes")
print(f"List of fruits after appending is {fruits}")


# extend -> function to add multiple elements at the end of list
fruits.extend(["watermelon", "papaya"])


# insert in list
fruits.insert(1, "guava")
print(f"List of fruits after inserting is {fruits}")

# remove from list
fruits.remove("banana")
print(f"List of fruits after removing is {fruits}")

# pop from list -> delete last element
fruits.pop()
print(f"List of fruits after poping is {fruits}")

# index -> Returns the index of first occurence of element
print(f"Index of orange is {fruits.index('orange')}")

