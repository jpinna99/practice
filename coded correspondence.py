#caesar cipher decode

string = "Ui sbqhe gku ub ugkyfe tu Uifqñq ui cuzeh gku ub ugkyfe tu Ydwbqjuhhq."
alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_decode_1(string_to_decode, offset):
    decoded_string = []
    for char in string_to_decode:
        if alphabet_lowercase.find(char) >= 0 or alphabet_uppercase.find(char) >= 0:
            char_value = alphabet_lowercase.find(char.lower())
        else:
            char_value = -1
        if char_value == -1:
            decoded_string.append(char)
        elif char_value + offset >= len(alphabet_lowercase) and char in alphabet_lowercase:
            decoded_string.append(alphabet_lowercase[char_value + offset - 26])
        elif char_value + offset >= len(alphabet_uppercase) and char in alphabet_uppercase:
            decoded_string.append(alphabet_uppercase[char_value + offset - 26])
        elif char in alphabet_lowercase:
            decoded_string.append(alphabet_lowercase[char_value + offset])
        elif char in alphabet_uppercase:
            decoded_string.append(alphabet_uppercase[char_value + offset])
    decoded_string_joined = "".join(decoded_string)
    return decoded_string_joined
print(caesar_decode_1(string, 10))

def caesar_decode_2(string_to_decode, offset):
    decoded_string = ""
    for char in string_to_decode:
        char_value_lower = alphabet_lowercase.find(char)
        char_value_upper = alphabet_uppercase.find(char)
        if char in alphabet_lowercase:
            decoded_string += alphabet_lowercase[(char_value_lower + offset) % len(alphabet_lowercase)]
        elif char in alphabet_uppercase:
            decoded_string += alphabet_uppercase[(char_value_upper + offset) % len(alphabet_uppercase)]
        else:
            decoded_string += char
    return decoded_string
print(caesar_decode_2(string, 10))


#caesar cipher encode
string = "Es claro que el equipo de España es mejor que el equipo de Inglaterra."
alphabet_lowercase = "abcdefghijklmnopqrstuvwxyz"
alphabet_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode_1(string_to_encode, offset):
    encoded_string = []
    for char in string_to_encode:
        if alphabet_lowercase.find(char) >= 0 or alphabet_uppercase.find(char) >= 0:
            char_value = alphabet_lowercase.find(char.lower())
        else:
            char_value = -1
        if char_value == -1:
            encoded_string.append(char)
        elif char_value - offset < 0 and char in alphabet_lowercase:
            encoded_string.append(alphabet_lowercase[char_value - offset + 26])
        elif char_value + offset < 0 and char in alphabet_uppercase:
            encoded_string.append(alphabet_uppercase[char_value - offset + 26])
        elif char in alphabet_lowercase:
            encoded_string.append(alphabet_lowercase[char_value - offset])
        elif char in alphabet_uppercase:
            encoded_string.append(alphabet_uppercase[char_value - offset])
    encoded_string_joined = "".join(encoded_string)
    return encoded_string_joined
print(caesar_encode_1(string, 10))

def caesar_encode_2(string_to_encode, offset):
    encoded_string = ""
    for char in string_to_encode:
        char_value_lower = alphabet_lowercase.find(char)
        char_value_upper = alphabet_uppercase.find(char)
        if char in alphabet_lowercase:
            encoded_string += alphabet_lowercase[(char_value_lower - offset) % len(alphabet_lowercase)]
        elif char in alphabet_uppercase:
            encoded_string += alphabet_uppercase[(char_value_upper - offset) % len(alphabet_uppercase)]
        else:
            encoded_string += char
    return encoded_string

print(caesar_encode_2(string, 10))

#vigenere cipher
message_to_decode = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
keyword = "friends"


def vigenere_decode(message_to_decode, keyword):
    keyword_phrase = ""
    counter = 0
    for character in message_to_decode:
        if character in alphabet_lowercase or character in alphabet_uppercase:
            keyword_phrase += keyword[counter % len(keyword)]
            counter += 1
        else:
            keyword_phrase += character

    decoded_message = ""
    for index in range(len(message_to_decode)):
        if message_to_decode[index] in alphabet_lowercase:
            value_char_to_add = (alphabet_lowercase.find(message_to_decode[index]) + alphabet_lowercase.find(
                keyword_phrase[index])) % len(alphabet_lowercase)
            decoded_message += alphabet_lowercase[value_char_to_add]
        elif message_to_decode[index] in alphabet_uppercase:
            value_char_to_add = (alphabet_uppercase.find(message_to_decode[index]) + alphabet_uppercase.find(
                keyword_phrase.upper()[index])) % len(alphabet_lowercase)
            decoded_message += alphabet_uppercase[value_char_to_add]
        else:
            decoded_message += message_to_decode[index]

    return decoded_message


print(vigenere_decode(message_to_decode, keyword))

message_to_encode = "you were able to decode this? nice work! you are becoming quite the expert at crytography!"
keyword = "friends"


def vigenere_encode(message_to_encode, keyword):
    keyword_phrase = ""
    counter = 0
    for character in message_to_encode:
        if character in alphabet_lowercase or character in alphabet_uppercase:
            keyword_phrase += keyword[counter % len(keyword)]
            counter += 1
        else:
            keyword_phrase += character

    encoded_message = ""
    for index in range(len(message_to_encode)):
        if message_to_encode[index] in alphabet_lowercase:
            value_char_to_add = (alphabet_lowercase.find(message_to_encode[index]) - alphabet_lowercase.find(
                keyword_phrase[index])) % len(alphabet_lowercase)
            encoded_message += alphabet_lowercase[value_char_to_add]
        elif message_to_encode[index] in alphabet_uppercase:
            value_char_to_add = (alphabet_uppercase.find(message_to_encode[index]) - alphabet_uppercase.find(
                keyword_phrase.upper()[index])) % len(alphabet_lowercase)
            encoded_message += alphabet_uppercase[value_char_to_add]
        else:
            encoded_message += message_to_encode[index]

    return encoded_message


encode_result = vigenere_encode(message_to_encode, keyword)
print(encode_result)
print(vigenere_decode(encode_result, keyword))