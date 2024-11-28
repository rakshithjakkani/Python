alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("what you want me to do: encode or decode?: ")
text = input(f"enter the text you want to {direction}: ")
shift_amount = int(input("enter the shift number to encrypt: "))

def encrypt(original_text, shift_num, encode_or_decode):
    encrypted_string = ""
    for i in original_text:
        if encode_or_decode == "decode":
            shift_num *= -1
        letter_index = alphabets.index(i) + shift_num
        letter_index %= len(alphabets)
        encrypted_string += alphabets[letter_index]
    print(f'Here is your {direction}d text: "{encrypted_string}"')
encrypt(text, shift_amount, direction)



