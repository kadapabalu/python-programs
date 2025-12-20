s = "Hello 123"
digits = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
spaces = sum(c.isspace() for c in s)
print(f"Digits: {digits}, Letters: {letters}, Spaces: {spaces}")
