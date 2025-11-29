# Write a function that takes a list of numbers and returns True if any number appears more than once,
# otherwise return false.
# Example:
# has_duplicates([1, 2, 3, 4])  # False
# has_duplicates([1, 2, 2, 3])  # True

num_list = [1,2,3,4,5,6,7,8]
# take num and compare that value to each other item in list
# repeat

def has_duplicates(num_list):
       # outlier for the first item in the list because it is always equal to itself
       have_seen = {}
       for num in num_list:
            if num in have_seen:
                return True
            else:
                have_seen[num] = "hotdog"
        return False
            
has_duplicates(num_list)
                                             
O(n^2)
num_list1 = [1,2,3,4,5,6,7]

def has_duplicates(num_list):
    new_list = []
    for num in num_list:
        if num in new_list:
            return True
        else:
            new_list.append(num)
    return False

print(has_duplicates(num_list))