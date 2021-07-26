student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Create a dictionary in this format:
nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}
#. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Ingrese la palabra que quiere NATear: ").upper()
user_input_list = [letter for letter in user_input]

output_dictionary = {letter: word for (letter, word) in nato_dictionary.items() if letter in user_input_list}
output_list = [nato_dictionary[letter] for letter in user_input_list ]
print(output_list)

