# inicialization of tuples
tuple_1 = (1, 2, 3, 4, 5)
print(f"Tuple 1 is {tuple_1}")

a, b, c, d, e = tuple_1
print(f"Value of a is {a}")


# how to ignore extra values in tuples with *_ operator
tuple_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first, *rest = tuple_2
print(f"First value is {first}")
print(f"Rest of values are {rest}")

tuple_3 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# create a sub tuple from tuple_3
sub_tuple = tuple_3[2:5]
print(f"Sub tuple is {sub_tuple}, using slicing")

# saber cuantas veces se repite un elemento en una tupla
tuple_4 = (1, 1, 1, 1, 2, 3, 4, 5, 6)
count_repeat = tuple_4.count(1)
print(f"El numero 1 se repite {count_repeat} veces")

# sum tuples
tuple_5 = (1, 2, 3, 4, 5)
tuple_6 = (6, 7, 8, 9, 10)
new_tuple = tuple_5 + tuple_6
print(f"New tuple is {new_tuple}")

# print(tuple_6 * 100)

# conver tuple to list
list_tuple = list(tuple_6)
print(f"List tuple is {list_tuple}")

# convertit una lista a tupla

tuple_list = tuple(list_tuple)
print(f"The list converted to tuple is {tuple_list}")

# for i in tuple_1:
#     print(i)

[print(i) for i in tuple_1]

# use tuples as key in dictionary
# ✅ Tuples can be used as keys if they contain only strings, numbers, or tuples;
names = {
    (1, 2): "John",
    (2, 3): "Doe",
    (3, 4): "Jane",
    (4, 5): "Doe",
}

print(f"Names are {names}")

print(f"Value of key (1, 2) is {names[(1, 2)]}")