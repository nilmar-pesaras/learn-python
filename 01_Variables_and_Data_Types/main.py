# variable declaration

'''
Variables are used to store data values.
'''

# Primitive Data Types
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

# Complex Data Types
list_var: list = [1, 2, 3]
tuple_var: tuple = (1, 2, 3)
dict_var: dict = {"name": "Mario", "age": 25}
set_var: set = {1, 2, 3}

# Type Checking
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of dict_var: {type(dict_var)}")

# Type Conversion
list_to_tuple = tuple(list_var) # convert list to tuple
tuple_to_list = list(tuple_var) # convert tuple to list
dict_to_set = set(dict_var) # convert dict to set

print(f"list_to_tuple: {list_to_tuple}")
print(f"tuple_to_list: {tuple_to_list}")
print(f"dict_to_set: {dict_to_set}")