to_translate = input("What would you like to translate to Pig Latin? ")
vowels = "aeiou"
alphabet = "abcdefghijklmnopqrstuvwxyz"

source = to_translate.lower()
source = source.split()

target = []

for word in source:
    for char in word:
        char_index = word.index(char)
        if char_index == 0 and char in vowels:
            translated_word = word + "-way"
            break
        elif char_index != 0 and char == "y":
            translated_word = "eye" + word[:char_index] + "-ay"
            break
        elif char == 'u' and word[char_index - 1] == "q":
            translated_word = word[char_index+1:] + "-" + "quay"
            break
        elif char in vowels:
            translated_word = word[char_index:] + "-" + word[:char_index].lower() + "ay"
            break
    for char in translated_word:
        if char not in alphabet and char != "-":
            char_to_remove = translated_word.index(char)
            translated_word = translated_word[:char_to_remove] + translated_word[char_to_remove+1:]
    target.append(translated_word)

translation = " ".join(target)
print(translation)