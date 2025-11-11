def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Return the index of the found element
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the element is not found

# Example usage
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
search_number = int(input("Enter the number that you want to search: "))
result = binary_search(sorted_numbers, search_number)

if result != -1:
    print(f"Number {search_number} found at index {result}.")
else:
    print(f"Number {search_number} does not exist.")