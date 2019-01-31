# Defining the Collection of Values
A = [12, 88, 9, 6, 5, 90, 61, 2, 31, 168, 47, 19]

# Defining the value to find
target = 90

print(A)
print('Our target is 90')


def search(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1


x = search(A, target)
print(x)
