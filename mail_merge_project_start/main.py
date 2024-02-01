PLACEHOLDER = "[name]"
with open("./mail_merge_project_start/input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open("./mail_merge_project_start/input/letters/starting_letter.txt") as letters_file:
    letter_context = letters_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_context.replace(PLACEHOLDER,stripped_name)
        with open(f"./mail_merge_project_start/output/ReadyToSend/letter_for_{stripped_name}.txt" , "w") as completed_letter:
            completed_letter.write(new_letter)    
