alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(c_direction, c_text, c_shift):
    plain_text = ""

    for letter in c_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if letter in alphabet:
            index_in_alphabet = alphabet.index(letter)
            offset = c_shift % 26
            if c_direction == "encode":
                new_index = index_in_alphabet + offset
                if new_index > 25:
                    new_index -= 26
            else:
                new_index = index_in_alphabet - offset
                if new_index < 0:
                    new_index += 26
            new_letter_alphabet = alphabet[new_index]
            plain_text += new_letter_alphabet
        else:
            plain_text += letter
    print(plain_text)

#TODO-1: Import and print the logo from art.py when the program starts.
from art_85 import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
game_continue = True

while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "encode" and direction != "decode":
        print("wrong input.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    option = input("Do you want to continue? yes or no. ").lower()

    while option != "yes":
        if option == "no":
            game_continue = False
            print("GoodBye")
            break
        elif option == 'yes':
            game_continue = True
        else:
            option = input("please select 'yes' or 'no'").lower()
    #
    # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # text = input("Type your message:\n").lower()
    # shift = int(input("Type the shift number:\n"))
    # caesar(direction, text, shift)
    # option = input("Do you want to contine? yes or no. ")

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#Hint: Think about how you can use the modulus (%).





# def encrypt(en_text, en_shift):
#     cipher_text_list = ""
#     plain_text_list = list(en_text)
#     #print(plain_text_list)
#
#     for letter_index_in_plain in plain_text_list:  #遍历plain_text
#         index_in_alphabet = alphabet.index(letter_index_in_plain)  #获取letter在alphabet的位置
#         #print(f"index_in_alphabet:{index_in_alphabet}")
#         new_index = index_in_alphabet + en_shift #做shift
#         if new_index > 25:
#             new_index -= 26
#         #print(f"new_index: {new_index}")
#         new_letter_alphabet = alphabet[new_index]   #获取在alphat中新的letter
#         #print(f"new_letter_alphabet: {new_letter_alphabet}\n")
#         cipher_text_list += new_letter_alphabet  #放在新list中
#     print(cipher_text_list)
#
# def decrypt(de_text, de_shift):
#     de_plain_text = ""
#     for letter_in_cipher in de_text:
#         de_index_in_alphabet = alphabet.index(letter_in_cipher)
#         #print(f"de_index_in_alphabet:{de_index_in_alphabet}")
#         de_new_index = de_index_in_alphabet - de_shift
#         if de_new_index < 0:
#             de_new_index += 26
#         de_new_letter_alphabet = alphabet[de_new_index]
#         de_plain_text += de_new_letter_alphabet
#     print(de_plain_text)
#
# if direction == "encode":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

