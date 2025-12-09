def bubble_sort(a, ascending=True):
    a = a[:]                # work on a copy
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if (ascending and a[j] > a[j+1]) or (not ascending and a[j] < a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

if __name__ == "__main__":
    nums = [5, 2, 9, 1, 5, 6]
    print("Original:", nums)
    print("Bubble ascending:", bubble_sort(nums, ascending=True))
    print("Bubble descending:", bubble_sort(nums, ascending=False))