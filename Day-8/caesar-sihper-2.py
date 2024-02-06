alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: ").lower()
text = input("enter the input text: ").lower()
shift = int(input("enter the shift index: "))

def encode(text_encode, shift_encode):
    cipher_text = ""
    for letters in text_encode:
        alphabet_index = alphabets.index(letters)
        shift_index = alphabet_index + shift_encode
        new_letter = alphabets[shift_index]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_decode):
    plain_text = ""
    for letters in cipher_text:
        possition = alphabets.index(letters)
        new_position = possition - shift_decode
        plain_text += alphabets[new_position]
    print(f"The decode text is: {plain_text}")


if direction == "encode":
    encode(text_encode=text, shift_encode=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_decode=shift)