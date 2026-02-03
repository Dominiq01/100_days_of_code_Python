student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (_, row) in nato_data.iterrows()}
print(new_dict)

no_error = False

while not no_error:
    user_input = list(input("Please write your name: ").upper())

    try:
        phonetic_code_list = [new_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        no_error = True
        print(phonetic_code_list)