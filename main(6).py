"""
3.1 Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found.
"""


def linear_search_product(products, target):
    indices = []
    for i in range(len(products)):
        if products[i] == target:
            indices.append(i)
    return indices


#Example usage:
products = ["apple", "banana", "orange", "banana", "grape"]
target = "banana"
result=linear_search_product(products, target)
print(result)
