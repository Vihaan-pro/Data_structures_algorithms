def insertion_sort(a, ascending=True):
    a = a[:]                # work on a copy
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        if ascending:
            while j >= 0 and a[j] > key:
                a[j+1] = a[j]
                j -= 1
        else:
            while j >= 0 and a[j] < key:
                a[j+1] = a[j]
                j -= 1
        a[j+1] = key
    return a

if __name__ == "__main__":
    nums = [5, 2, 9, 1, 5, 6]
    print("Original:", nums)
    print("Insertion ascending:", insertion_sort(nums, ascending=True))
    print("Insertion descending:", insertion_sort(nums, ascending=False))