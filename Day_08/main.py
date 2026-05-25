# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shift_text_index = alphabet.index(letter) + shift_amount
            shift_text_index %= len(alphabet)
            shift_text = alphabet[shift_text_index]
            output_text += shift_text

    print(f"Here is the {encode_or_decode}d text: {output_text}")



# A way to restart the cipher program?

ask_continue = True

while ask_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    replay = input("Do you want to continue with encoding and decoding? If Yes, type yes, if no type no.\n").lower()
    if replay == "no":
        ask_continue = False
        print("GOODBYE!")


