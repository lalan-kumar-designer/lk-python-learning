# Regular Expressions

# Import re to search and match text patterns.
import re

# Search for a word in a string.
text = "Python Programming"
result = re.search("Python", text)
print(result.group() if result else "Not Found")

# Find all numbers in a string.
text = "My marks are 75 and 85"
print(re.findall(r"\d+", text))

# Check whether a string starts with a word.
text = "Python is easy"
result = re.match("Python", text)
print(result.group() if result else "No Match")

# Replace a word in a string.
text = "I like Java"
print(re.sub("Java", "Python", text))

# Check whether a string contains only digits.
text = "12345"
print(bool(re.fullmatch(r"\d+", text)))