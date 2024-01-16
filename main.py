import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
word = input("Enter a word:\n").upper()
letter_list = [letter for letter in word]
code_words = [data_dict[letter] for letter in letter_list]
print(code_words)