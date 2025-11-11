def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Example usage
numbers = [7, 100, 3, 4, 5, 6, 111100, 700, 900, 200, 5500, 600, 234567890, 987654321, 400, 600, 156]
search_number = int(input("Enter the number that you want to search: "))
result = linear_search(numbers, search_number)

if result != -1:
    print(f"Number {search_number} found at index {result}.")
else:
    print(f"Number {search_number} does not exist.")