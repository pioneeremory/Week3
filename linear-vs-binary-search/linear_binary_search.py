# # Linear Search
# def linear_search_unsorted(arr, target):
#     count = 0
#     for i, element in enumerate(arr):
#         count +=1
#         if element == target:
#             return i
#     return -1, count

# # print(linear_search_unsorted([1,1,2,3,2,1,5], 5))

# # Binary Search
# def binary_search_unsorted(arr, target):
#     sorted_list = sorted(arr)

#     counter = 0
#     low, high = 0, len(sorted_list) -1
#     while low <= high:
#         counter += 1
#         mid = (low + high) //2
#         if sorted_list[mid] == target:
#             return mid, counter
#         elif sorted_list[mid] < target:
#             low = mid + 1
#         else:
#             high = mid -1
#     return -1, counter

# # print(binary_search_unsorted([1,1,2,3,2,1,5], 5))

# Scenario 1 Test
# unsorted_list = [42, 15, 7, 30, 22, 10, 18]
# target_1 = 30
# result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
# result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
# print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
# print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")

# Linear Search
# def linear_search_sorted_words(word_list, target_word):
#     count = 0
#     for i in range(len(word_list)):
#         count += 1
#         if word_list[i] == target_word:
#             return i, count
#     return False

# # print(linear_search_sorted_words(["apple", "banana", "pear"], "pear"))

# # Binary Search
# def binary_search_sorted_words(word_list, target_word):
#     count = 0
#     low, high = 0, len(word_list) -1
#     while low <= high:
#         count += 1
#         mid = (low + high) //2
#         if word_list[mid] == target_word:
#             return mid, count
#         elif word_list[mid] < target_word:
#             low = mid + 1
#         else:
#             high = mid -1
#     return target_word, count

# # Scenario 2 Test
# sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
# target_2 = 'orange'
# result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
# result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
# print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
# print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")

# Linear Search
def linear_search_last_occurrence(arr, target):
    count = 0                                          # ← initialize!
    for i in range(len(arr) -1, -1, -1):              # ← perfect backward loop
        count += 1
        if arr[i] == target:                           # ← compare value, not index!
            return i, count
    return -1, count

# Binary Search
def binary_search_last_occurrence(arr, target):
    count = 0
    low, high = 0, len(arr) -1
    while low <= high:
        count += 1
        mid = (low + high) //2
        if arr[mid] == target:
            return mid, count
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return target, count

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")