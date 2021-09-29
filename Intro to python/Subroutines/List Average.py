nums = [1,2,4,9,12,15,16,17]

def total(numbers):
    total = 0
    for item in nums:total += item
    return total

def average(numbers):
    return total(numbers)/len(numbers)

print("Total =", total(nums))
print("Average =", average(nums))