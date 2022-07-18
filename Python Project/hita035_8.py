# To count number of strings that start and end with same character

# Function to count the string with given parameters
def match_words(words):
  
# Initializing count as 0
  cnt = 0

# Iterating a for loop to count the string with given parameters
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      cnt += 1
# Returning the count value
  return cnt

# Printing the count value by calling the function and returning the count in print
print(match_words(['abc', 'xyz', 'aba', '1221']))







