# Big O notation
# O(n!): Represents factorial time complexity, where the efficiency grows factorially with the input size.
# O(2^n): Denotes exponential time complexity, commonly seen in algorithms with recursive branching.
# O(n²): Signifies quadratic time complexity, indicating that the efficiency grows with the square of the input size.
# O(n log n): Represents linearithmic time complexity, commonly observed in efficient sorting algorithms like mergesort and heapsort.
# O(n): Indicates linear time complexity, where the efficiency scales linearly with the input size.
# O(log n): Denotes logarithmic time complexity, common in algorithms like binary search.
# O(1): Represents constant time complexity, indicating consistent efficiency regardless of the input size.
arr1 = [1, 2, 3, 4, 5, 6, 7, 10]

# O(n)
def largest(array, value):
    count = 0
    for item in array:
        if item > value:
            count += 1
    return count


print(largest(arr1, 2))

customers = ["Logan", "Sally", "Richard"]

def info_dump(customers):
  count2 = 0
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
    count2 +=1
    return count2
  count3 = 0 
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
    count3 += 1
    return count3
  