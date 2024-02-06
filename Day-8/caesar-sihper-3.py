alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt: ").lower()
text = input("enter the input text: ").lower()
shift = int(input("enter the shift index: "))

def caesar_sipher(start_text, shift_amount, caesar_direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabets.index(letter)
        new_position = position + shift_amount
        end_text += alphabets[new_position]
    print(f"Here is the {caesar_direction}d result: {end_text}")

caesar_sipher(start_text=text, shift_amount=shift, caesar_direction=direction)

