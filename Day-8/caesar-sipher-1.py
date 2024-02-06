alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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

encode(text_encode=text, shift_encode=shift)