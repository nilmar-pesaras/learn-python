# variable declaration

# dynamic variable declaration
name = "Super Mario"
age = 20
print(f"Name: {name} and Age: {age}")


# variable declaration with type hinting
name: str = "Super Mario"
age: int = 20
height_in_m: float = 100.9
is_alive: bool = True
print(f'''
Name: {name},
Age: {age},
Height: {height_in_m},
Is Alive: {is_alive}
''')


# list declaration with type hinting

'''
the string value "5" will be converted to integer.
Thus this will return [1, 2, 3, 4, 5] as integers
'''

numbers: list[str] = [1, 2, 3, 4, "5"] 
print(numbers)

list = [1,2,3,4,5]
list.append(6)
print(list) # [1, 2, 3, 4, 5, 6]

# list methods

# append
list.append(7)
print(f'New list after adding "7": {list}') # [1, 2, 3, 4, 5, 6, 7]

# remove
list.remove(7)
print(f'New list after removing "7": {list}') # [1, 2, 3, 4, 5, 6]

# dictionary declaration with type hinting

dict_numbers: dict = {
    "one": "1",
    "two": "2",
    "three": "3"
}
print(dict_numbers)
