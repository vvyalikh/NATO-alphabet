
import pandas


#option 1(my own)
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# nato_letter = nato["letter"].to_list()
# nato_code = nato["code"].to_list()
# #nato_dict = dict(zip(nato_letter, nato_code))
# nato_dict = {key:value for key, value in zip(nato_letter, nato_code)}
# user_word = "JEVGENIJS"
#
#
# word_spelled = {}


# for letter in user_word:
#     for key, value in nato_dict.items():
#         if letter == key:
#             word_spelled[letter] = value

# print(word_spelled)

#option 2(based on solution)
#TODO 1. Create a dictionary in this format:

nato_dict = {row.letter:row.code for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter the word: ").upper()
output_word = [nato_dict[letter] for letter in word]
print(output_word)



