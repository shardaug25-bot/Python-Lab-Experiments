text = input("Enter a text string: ")

# Word frequency
words = text.split()
word_frequency = {}

for word in words:
    word = word.lower()
    word_frequency[word] = word_frequency.get(word, 0) + 1

print("\nWord Frequency:")

for word, count in word_frequency.items():
    print(word, ":", count)

# Character frequency
character_frequency = {}

for ch in text:
    if ch != " ":
        character_frequency[ch] = character_frequency.get(ch, 0) + 1

print("\nCharacter Frequency:")

for ch, count in character_frequency.items():
    print(ch, ":", count)