from operator import indexOf

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(original_text,shift_amount):
    encrypted_code =""


# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

    for i in original_text:
        try:
            shifted_index = alphabet.index(f"{i}")+shift_amount
            if alphabet[shifted_index] in list:
                encrypted_code+=alphabet[shifted_index]
        except IndexError:
            encrypted_code += alphabet[(-len(alphabet)+alphabet.index(f"{i}")) + shift_amount  ]

    print(encrypted_code)








# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text,shift)