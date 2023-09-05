# ----------------- Ordering methods ----------------- #

# create random numeric list of 15 elements
random_numbers = [1, 5, 2, 3, 4, 6, 7, 8, 9, 10, 15, 12, 13, 14, 11]
print(f"Original list of numbers is {random_numbers}")


# sort -> sort the list in ascending order
ascending_numbers = sorted(random_numbers)
random_numbers_asc = random_numbers.sort()
print(f"Ascending order of numbers is {ascending_numbers}")

# zip -> function to combine two lists
numbers = [1, 2, 3, 4, 5]
names = ["John", "Doe", "Jane", "Doe", "Jack"]

# zip function combines two lists
number_list = list(zip(numbers, names))
print(f"Combined list is {number_list}")

# Map -> function to apply a function on all elements of list
# create a function to square numbers list

squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers are {squared_numbers}")


# list of words
words = ["apple", "banana", "orange", "mango", "grapes"]

# funtion to count length of string
def len_of_string(string):
    return len(string)

conteo_de_letras = map(len_of_string, words)
lista_de_conteo = list(conteo_de_letras)

print(f"Lista de conteo de letras es {lista_de_conteo}")