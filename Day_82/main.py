from morse_dict import MORSE_CODE_DICT

def translate_to_morse(string_to_morse):
    final_string = ''
    for letter in string_to_morse:
        big_letter = letter.upper()
        final_string += MORSE_CODE_DICT[big_letter] + " "

    return final_string.strip()

user_string = input("What is your message?: ")

final_string = translate_to_morse(user_string)

print(f"Here is your coded message: {final_string}")

