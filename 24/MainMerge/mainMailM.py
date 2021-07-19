# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Importo la carta
with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()

# importo los nombres y creo una lista
with open("Input/Names/invited_names.txt") as invited_names:
    list_of_names = invited_names.readlines()

new_letter = letter.replace("[name]", "David")
print(new_letter)


def generate_letter(new_letter, name):
    letter_path = f"Output/ReadyToSend/letter_for_{name}.txt"
    with open(letter_path, mode="w") as letter_content:
        letter_content.write(new_letter)


for name in list_of_names:
    new_letter = letter.replace("[name]", name.strip())
    generate_letter(new_letter=new_letter, name=name)
