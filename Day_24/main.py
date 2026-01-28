#TODO: Create a letter using starting_letter.txt 

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()
    for name in invited_names:
        with open("./Input/Letters/starting_letter.txt") as letter:
            content = letter.read()
        with open(f"./Output/ReadyToSend/letter_for_{name.rstrip()}.docx", mode="w") as new_letter:
            content = content.replace("[name]", name.rstrip())
            new_letter.write(content)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp