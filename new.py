def messy_function(lst):
    total = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            total = total + lst[i] ** 2
        else:
            total = total - lst[i] * 2
    return total

# Example usage
nums = [1, 2, 3, 4, 5, 6]
print(messy_function(nums))
