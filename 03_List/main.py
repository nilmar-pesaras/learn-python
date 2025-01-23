# List

vegetables: list[str] = [
    "potato",
    "tomato",
    "carrot",
    "cabbage"
]

print(f"Vegetables: {vegetables}")

# Using List Built-in methods

# Length of the list
print(f"Length of the list: {len(vegetables)}")

# Adding new item to the list
vegetables.append("onion")
print(f"Vegetables: {vegetables}")

# Adding multiple items to the list
vegetables.extend(["broccoli", "spinach", "lettuce"])
print(f"Vegetables: {vegetables}")

# Replacing item in the list
vegetables[0] = "sweet potato" # using indexing
print(f"Vegetables: {vegetables}")

