# Example of searching for strings using linear search
def linear_search_strings(arr, target):
    for i in range(len(arr)):
        if arr[i].lower() == target.lower():  # Case insensitive search
            return i
    return -1

# Example usage
words = ["Banana", "apple", "Cherry", "date", "Elderberry"]
search_word = input("Enter the word that you want to search: ")
result = linear_search_strings(words, search_word)

if result != -1:
    print(f"Word '{search_word}' found at index {result}.")
else:
    print(f"Word '{search_word}' does not exist.")