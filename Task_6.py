# Write a script to check whether a specified value is contained in a group of values.

def is_group_member(group_data, n):
    return n in group_data
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
