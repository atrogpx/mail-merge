with open("Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
with open("Input/Letters/starting_letter.txt") as main_letter:
    m_letter = main_letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = m_letter.replace("[name]", stripped_name)
        with open(f"Output/ReadyToSend/LetterTo{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)


#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".