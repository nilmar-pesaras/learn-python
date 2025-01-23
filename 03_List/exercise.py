# You have a fun road trip across Europe that starts in a few days. You will fly into London and then drive to Paris, Munich, and Venice.

# Part A
'''
Create a list named packing_list with the following initial items: passport, clothes, and sunglasses.
'''
packaging_list: list[str] = ["passport", "clothes", "sunglasses"]


# Part B
'''
You realize you'll need a few more items for your journey. Add a toothbrush and a phone charger to your packing list.
'''
packaging_list.extend(["toothbrush", "phone charger"])

# Part C
'''
You decide you also want to bring a book. Since you left your book near your sunglasses on your kitchen table, you will pack them together. Insert "book" after sunglasses in your packing list.
'''
packaging_list.insert(packaging_list.index("sunglasses") + 1, "book")

# Part D
'''
You walk around your house gathering the items you will need for your trip. Unfortunately, you can't seem to find your sunglasses. Remove "sunglasses" from your packing list.
'''
packaging_list.remove("sunglasses")
print(packaging_list)