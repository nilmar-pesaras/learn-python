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
