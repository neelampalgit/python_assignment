def product_array(arr):
    product = 1
    for num in arr:
        product *= num
    return product

arr = [1, 2, 3, 4, 5]
print(product_array(arr))  # Output: 120
