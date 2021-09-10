list_num = []
list_num.extend([1, 2])  # extending list elements
print(list_num)
list_num.extend((3, 4, 5.5, 6.8))  # extending tuple elements
print(list_num)
list_num.extend('ABC')  # extending string elements
print(list_num)

evens = [2, 4, 6]
odds = [1, 3, 5]

nums = odds + evens
print(nums) 