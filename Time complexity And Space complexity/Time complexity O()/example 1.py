# O(n) - Linear time
def print_all(arr):
    for i in range(len(arr)):
        print(arr[i])

# O(n^2) - Quadratic time
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

arr = [1, 2, 3]

print("=== print_all(arr) - O(n) ===")
print_all(arr)

print()
print("=== print_pairs(arr) - O(n^2) ===")
print_pairs(arr)