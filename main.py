# TODO Create a script to turn strings into morse code.

# Dictionary for morse code
from morsecode import MORSE_CODE_DICT


def encrypt(message):
    new_list = " "
    for letter in message:
        if letter in MORSE_CODE_DICT:
            new_list += MORSE_CODE_DICT[letter] + " "
        else:
            new_list += " "
    return new_list


def decode(letter):
    for key, value in MORSE_CODE_DICT.items():
        if letter in value:
            return key



def main():
    user_input = input("Hello User! "
                       "Please enter the word or sentence that you would like to have converted to Morse Code: ")
    result = encrypt(user_input.upper())
    print(result)

    new_result = " "
    for letter in result:
        new_result += letter
    print(decode(new_result))



if __name__ == '__main__':
    main()
