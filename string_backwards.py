# iterate over a string backwards using while
text = "abcdefghijkl"
i = 0
while i < len(text):
    print(text[len(text)-1-i])
    i += 1