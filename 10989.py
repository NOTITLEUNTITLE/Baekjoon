def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    pivot = len(array) // 2
    left = merge_sort(array[:pivot])
    right = merge_sort(array[pivot:])

    return merge(left, right)
            

def heap_sort(a):
    for i in range(1,len(a)):
        c = i
        while c != 0:
            r = (c-1) // 2
            if a[r] < a[c]:
                a[r], a[c] = a[c], a[r]
            c = r

    for i in range(len(a)-1,-1,-1):
        a[0], a[i] = a[i], a[0]
        r = 0
        c = 1
        while c < i:
            c = 2*r + 1
            if c < i -1 and a[c] < a[c+1]:
                c += 1
            if c < i and a[r] < a[c]:
                a[r], a[c] = a[c], a[r]
            r = c
N = int(input())
data = list()
for i in range(N):
    data.append(int(input()))

# heap_sort(data)
# print(merge_sort(data))
data = merge_sort(data)
for d in merge_sort(data):
    print(d)



# N = int(input())
# num = []

# for i in range(N):
#     num.append(int(input()))

# num = sorted(num)

# for i in num:
#     print(i)
