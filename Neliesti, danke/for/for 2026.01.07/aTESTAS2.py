txt = "Python programa mokytis smagu"
word = ""

for char in txt:
    if char == " ":
        print(word)
        word = ""
    else:
        word += char
print(word)
