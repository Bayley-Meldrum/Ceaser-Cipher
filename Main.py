
message = input("Enter a message: ")

shift = int(input("Enter your secret number: "))

def shift_message(message, shift):
    shifted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            shifted_char = char
        shifted_message += shifted_char
    return shifted_message

print(shift_message(message, shift))
